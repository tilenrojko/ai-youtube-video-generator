import json
import os
import random
from abc import abstractmethod
from datetime import datetime
from googleapiclient.http import MediaFileUpload
from youtube_api_service import create_service

TIMEOUT = 30000
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_NAME = 'youtube'
API_VERSION = 'v3'


class GenericYoutubeGenerator:
    def __init__(self, root_path, weekly_upload_folder_path):
        self.API_NAME = API_NAME
        self.API_VERSION = API_VERSION
        self.SCOPES = SCOPES
        self.socket_timeout = TIMEOUT
        self.upload_date_file_path = root_path + "/last_upload_date.json"
        self.upload_date_json_key = "lastUploadDate"
        if os.path.isdir(self.upload_date_file_path):
            self.upload_date = self.read_datetime_from_json(self.upload_date_file_path)
        else:
            self.upload_date = datetime.now()
            self.read_datetime_from_json(self.upload_date_file_path)
        self.root_path = root_path
        self.weekly_upload_folder_path = weekly_upload_folder_path
        self.youtube_names_json_path = self.root_path + "\\youtube_names.json"
        self.CLIENT_SECRET_FILE = self.root_path + "/client_secret.json"
        self.generator_pickle_name = self.get_pickle_name()
        self.service = create_service(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.generator_pickle_name, self.SCOPES)

    def set_upload_date(self, _upload_date):
        self.upload_date = _upload_date
        self.write_datetime_to_json(_upload_date)

    def read_datetime_from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if self.upload_date_json_key not in data:
                    raise ValueError(f"Key '{self.upload_date_json_key}' not found in the JSON file.")
                datetime_str = data.get(self.upload_date_json_key)
                if datetime_str:
                    return datetime.fromisoformat(datetime_str)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error reading datetime from JSON: {e}")
        except FileNotFoundError:
            print(f"File not found. Writing current datetime to {self.upload_date_file_path}.")
            self.write_datetime_to_json(datetime.now())
            #self.upload_date = datetime.now()
        return None

    def write_datetime_to_json(self, datetime_obj):
        try:
            with open(self.upload_date_file_path, 'w') as file:
                json.dump({self.upload_date_json_key: datetime_obj.isoformat()}, file)
        except (TypeError, FileNotFoundError) as e:
            print(f"Error writing datetime to JSON: {e}")


    def get_description_template(self):
        return """
{descriptionstart}

Title: {songtitle}
Download link: {url}

🔑 Licensing Details - Enjoy Creating with Freedom!

🌟 Download For Free During Your Trial Period:

Unlimited Access: Feel free to create and publish as much content as you like on your
registered channels using music from VidAssets during the trial period.
Monetization Clearance: Good news! Any content you publish during the trial is cleared for
monetization. Keep earning from your creative work without worries. After the trial ends, the published content
remains cleared, but the downloaded tracks cannot be used for new content.
One-Time Use Per Track: To keep your content fresh and unique, each downloaded track from
VidAssets can be used in one published content piece only. It encourages a diverse and ever-changing soundscape for your channel!

The monetary support that we get really helps support the creators, so that they can provide premium quality music and SFX in the future!

🎶 Keep Creating, Keep Inspiring!:
Our goal is to make your creative journey as smooth and enjoyable as possible. We're here to
provide the soundtrack; you bring the vision to life!
If you have any questions or need more details about our licensing, feel free to reach out at https://www.vidassets.io/contact. We're always here to help!


📢 Stay Updated:
Don't forget to subscribe and hit the bell icon to stay updated with our latest uploads.

📣 Follow Us For More Amazing Music:
VidAssets: https://www.vidassets.io/

💬 Your Thoughts:
We love hearing from you! Share your thoughts about this track in the comments below. Let us know what type of music you'd like to hear next on our channel.

💌 Contact:
For inquiries, suggestions, or collaborations, reach out to us at https://www.vidassets.io/contact.

🎧 Enjoy the music!
        """


    def custom_url_encoding(self, url):
        return url.replace(' ', '%20')

    def create_vidassets_url(self, folder_name) -> str:
        return r"https://www.vidassets.io/dashboard/music/search?name=" + self.custom_url_encoding(folder_name)

    def get_youtube_video_name(self) -> str | None:
        with open(self.youtube_names_json_path, 'r') as file:
            data_list = json.load(file)
        if not data_list:
            return None
        chosen_entry = random.choice(data_list)
        data_list.remove(chosen_entry)
        with open(self.youtube_names_json_path, 'w') as file:
            json.dump(data_list, file, indent=4)
        return chosen_entry

    def select_tags(self, tags: list[str], char_limit=200) -> list:
        selected_tags = []
        current_length = 0
        while current_length < char_limit:
            tag = random.choice(tags)
            if current_length + len(tag) + 1 <= char_limit:
                selected_tags.append(tag)
                current_length += len(tag) + 1
            else:
                break
        return selected_tags

    def get_subfolder_paths(self) -> list:
        subfolder_paths = []
        for root, dirs, files in os.walk(self.weekly_upload_folder_path):
            for dir in dirs:
                subfolder_path = os.path.join(root, dir)
                subfolder_paths.append(subfolder_path)
        return subfolder_paths
    
    def get_youtube_tags(self) -> list:
        tags = self.get_random_tags_list()
        random_tags = self.select_tags(tags)
        standardized_tags = self.get_standard_tag_list()
        return random_tags + standardized_tags

    def upload_video(self, request_body, weekly_upload_folder_path):
        print(self.service)
        render_path = os.path.join(weekly_upload_folder_path, "render.mp4")
        media_file = MediaFileUpload(render_path)
        thumbnail_path = os.path.join(weekly_upload_folder_path, "thumbnail.jpg")
        response_upload = self.service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media_file
        ).execute()
        # Thumbnail upload code (commented out)
        # self.service.thumbnails().set(
        #    videoId=response_upload.get('id'),
        #    media_body=MediaFileUpload(thumbnail_path)
        # ).execute()

    def create_youtube_description(self, song_name) -> str:
        description_template = self.get_description_template()
        return description_template.format(url=self.create_vidassets_url(song_name), songtitle=song_name, descriptionstart=self.get_description_start())

    @abstractmethod
    def get_description_start(self) -> str:
        pass

    @abstractmethod
    def get_random_tags_list(self) -> list:
        pass

    @abstractmethod
    def get_standard_tag_list(self) -> list:
        pass

    @abstractmethod
    def get_midjourney_prompt(self) -> str:
        pass

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def get_genre(self):
        pass

