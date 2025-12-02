from youtube_channels.cinematic_youtube_channels.generic_cinematic_trailer_generator import \
    GenericCinematicTrailerGenerator

class TrailermaxxYoutubeGenerator(GenericCinematicTrailerGenerator):
    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/cinematic_youtube_channels/cinematic_trailermaxx_channel"
        super().__init__(root_path)

    def get_pickle_name(self):
        return "trailermaxx_pickle"

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "inspiring landscape shot, real photography, insane details, epic scale, visually stunning, wallpaper, negative space in center, deep colours --ar 16:9 "