from abc import abstractmethod
from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericLofiYoutubeGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/lofi_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "chill lofi study wallpaper --ar 16:9"

    def get_standard_tag_list(self):
        return ["no copyright music", "no copyright lofi music", "chill", "vlog"]

    def get_random_tags_list(self):
        tags = [
            "chill no copyright music", "lofi no copyright music", "copyright free lofi chill vlog music"
            , "free lofi chill vlog music"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Chill Lofi Hip Hop No Copyright Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "lofi"
