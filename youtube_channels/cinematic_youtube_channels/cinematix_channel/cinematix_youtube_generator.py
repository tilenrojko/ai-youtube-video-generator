from youtube_channels.cinematic_youtube_channels.generic_cinematic_trailer_generator import \
    GenericCinematicTrailerGenerator


class CinematixYoutubeGenerator(GenericCinematicTrailerGenerator):
    def get_pickle_name(self):
        return "cinematix_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/cinematic_youtube_channels/cinematix_channel"
        super().__init__(root_path)

    def get_midjourney_prompt(self):
        return "inspiring cinematic nature, real photography, insane details, epic scale, visually stunning, wallpaper, negative space in center --ar 16:9"

    def get_email(self):
        return "vidassetsmusic@gmail.com"
