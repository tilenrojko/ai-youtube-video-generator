from abc import abstractmethod
from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericRockYoutubeGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/rock_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "realistic dynamic and immersive wallpaper a vehicle, set against a uniquely cool and realistic backdrop. --ar 16:9 --v 6.0 --s 50 --style raw"

    def get_standard_tag_list(self):
        return ["no copyright rock music", "no copyright rock music"]

    def get_random_tags_list(self):
        tags = [
            "rock no copyright music", "no copyright rock music", "copyright free rock music"
            , "free rock no copyright music", "free music"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Rock No Copyright Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "rock"

