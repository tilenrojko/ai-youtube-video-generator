from abc import ABC

from youtube_channels.lofi_youtube_channels.generic_lofi_youtube_generator import GenericLofiYoutubeGenerator


class ChillCafeVibesYoutubeGenerator(GenericLofiYoutubeGenerator):
    def get_pickle_name(self):
        return "chill_cafe_vibes_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/lofi_youtube_channels/lofi_chill_cafe_vibes_channel"
        super().__init__(root_path)

    def get_email(self):
        return "onymusicgroup@gmail.com"
