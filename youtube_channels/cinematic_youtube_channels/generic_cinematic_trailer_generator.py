from abc import abstractmethod

from youtube_channels.generic_youtube_generator import GenericYoutubeGenerator


class GenericCinematicTrailerGenerator(GenericYoutubeGenerator):
    def __init__(self, root_path):
        weekly_upload_folder_path = "X:/PyCharm/youtube_bot/youtube_channels/cinematic_youtube_channels/weekly_upload_folders"
        super().__init__(root_path, weekly_upload_folder_path)

    def get_midjourney_prompt(self):
        return "epic inspiring cinematic, real photography, insane details, epic scale, visually stunning, wallpaper --ar 16:9 --v 6.0 --style raw --s 50 --w 1"

    def get_standard_tag_list(self):
        return ["no copyright music", "no copyright cinematic music", "trailermaxx"]

    def get_random_tags_list(self):
        tags = [
            "no copyright music",
            "non copyrighted music",
            "cinematic no copyright music",
            "epic background music no copyright",
            "cinematic background music no copyright",
            "cinematic background music",
            "cinematic music no copyright",
            "battle no copyright music",
            "epic cinematic no copyright music",
            "action no copyright music",
            "dramatic no copyright soundtrack",
            "orchestral no copyright music",
            "intense background music no copyright",
            "trailer music no copyright",
            "adventure no copyright music",
            "heroic no copyright score"
        ]
        return tags

    def get_description_start(self):
        return "🎶 Epic Cinematic Trailer Music For Your Videos!"

    @abstractmethod
    def get_pickle_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    def get_genre(self):
        return "cinematic"
