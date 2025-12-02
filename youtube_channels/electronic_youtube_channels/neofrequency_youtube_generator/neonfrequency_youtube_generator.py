from youtube_channels.electronic_youtube_channels.generic_electronic_youtube_generator import \
    GenericElectronicYoutubeGenerator


class NeonfrequencyYoutubeGenerator(GenericElectronicYoutubeGenerator):
    def get_pickle_name(self):
        return "neonfrequency_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/electronic_youtube_channels/neofrequency_youtube_generator"
        super().__init__(root_path)

    def get_email(self):
        return "vidassetsmusic@gmail.com"