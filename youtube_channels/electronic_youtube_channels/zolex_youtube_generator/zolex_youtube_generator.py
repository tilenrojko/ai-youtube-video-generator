from youtube_channels.electronic_youtube_channels.generic_electronic_youtube_generator import \
    GenericElectronicYoutubeGenerator


class ZolexYoutubeGenerator(GenericElectronicYoutubeGenerator):
    def get_pickle_name(self):
        return "zolex_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/electronic_youtube_channels/zolex_youtube_generator"
        super().__init__(root_path)

    def get_email(self):
        return "onymusicgroup@gmail.com"