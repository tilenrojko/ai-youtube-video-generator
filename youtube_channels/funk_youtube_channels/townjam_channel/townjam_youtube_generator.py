from youtube_channels.funk_youtube_channels.generic_funk_youtube_generator import \
    GenericFunkYoutubeGenerator


class TownjamYoutubeGenerator(GenericFunkYoutubeGenerator):
    def get_pickle_name(self):
        return "townjam_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/funk_youtube_channels/townjam_channel"
        super().__init__(root_path)

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "vibrant funk wallpaper, warm, 8k --v 6.0 --s 50 --style raw --ar 16:9"
