from abc import abstractmethod
from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericHipHopYoutubeGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/hip_hop_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "illustration, in the style of hip hop aesthetics, light gray and amber, interior scenes, colorful moebius, floralpunk, raw documentation, dau-al-set --v 6.0 --s 50 --style raw --ar 16:9"

    def get_standard_tag_list(self):
        return ["no copyright hip hop music", "no copyright hip hop music", "chill", "vlog"]

    def get_random_tags_list(self):
        tags = [
            "chill no copyright music", "hip hop no copyright music", "copyright free hip hop chill vlog music"
            , "free hip hop chill vlog music"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Chill Hip Hop No Copyright Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "hiphop"

