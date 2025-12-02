from youtube_channels.corporate_youtube_channels.generic_corporate_youtube_generator import \
    GenericCorporateYoutubeGenerator


class PulseproYoutubeGenerator(GenericCorporateYoutubeGenerator):
    def get_pickle_name(self):
        return "pulsepro_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/corporate_youtube_channels/pulsepro_channel"
        super().__init__(root_path)

    def get_email(self):
        return "onymusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "corporate business wallpaper --ar 16:9 --v 6.0 --s 50 --style raw"