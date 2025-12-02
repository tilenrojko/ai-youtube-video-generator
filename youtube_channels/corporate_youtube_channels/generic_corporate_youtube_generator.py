from abc import abstractmethod
from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericCorporateYoutubeGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/corporate_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "corporate skyline wallpaper --ar 16:9 --v 6.0 --s 50 --style raw"

    def get_standard_tag_list(self):
        return ["no copyright corporate music", "corporate music"]

    def get_random_tags_list(self):
        tags = [
            "corporate no copyright music", "no copyright corporate music", "copyright free corporate music"
            , "free corporate music"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Corporate No Copyright Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "corporate"

