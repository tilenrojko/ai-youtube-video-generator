from abc import abstractmethod
from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericPopYoutubeGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/pop_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "inspiring pop video still, in the style of real photography --v 6.0 --s 50 --style raw --ar 16:9"

    def get_standard_tag_list(self):
        return ["no copyright pop music", "pop music"]

    def get_random_tags_list(self):
        tags = [
            "pop no copyright music", "no copyright pop music", "copyright free pop music"
            , "free pop music"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Pop No Copyright Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "pop"

