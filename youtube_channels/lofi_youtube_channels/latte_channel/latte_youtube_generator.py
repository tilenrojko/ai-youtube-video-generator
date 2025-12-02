from abc import ABC

from youtube_channels.lofi_youtube_channels.generic_lofi_youtube_generator import GenericLofiYoutubeGenerator


class LatteYoutubeGenerator(GenericLofiYoutubeGenerator):
    def get_pickle_name(self):
        return "latte_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/lofi_youtube_channels/latte_channel"
        super().__init__(root_path)

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "chill lofi city wallpaper --ar 16:9"
