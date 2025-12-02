from youtube_channels.corporate_youtube_channels.generic_corporate_youtube_generator import \
    GenericCorporateYoutubeGenerator


class CSkylineYoutubeGenerator(GenericCorporateYoutubeGenerator):
    def get_pickle_name(self):
        return "cskyline_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/corporate_youtube_channels/cskyline_channel"
        super().__init__(root_path)

    def get_email(self):
        return "vidassetsmusic@gmail.com"

    def get_midjourney_prompt(self):
        return "corporate skyline wallpaper --ar 16:9 --v 6.0 --s 50 --style raw"
