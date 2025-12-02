from abc import abstractmethod
from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericFunkYoutubeGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/funk_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "wallpaper in the style of poster art, 32k uhd, harlem renaissance, website, warm, 8k --v 6.0 --s 50 --style raw --ar 16:9"

    def get_standard_tag_list(self):
        return ["no copyright funk music", "funk music"]

    def get_random_tags_list(self):
        tags = [
            "funk no copyright music", "no copyright funk music", "copyright free funk music"
            , "free funk music"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Funk No Copyright Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "funk"

