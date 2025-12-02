from youtube_channels.funk_youtube_channels.generic_funk_youtube_generator import \
    GenericFunkYoutubeGenerator


class FunktasticYoutubeGenerator(GenericFunkYoutubeGenerator):
    def get_pickle_name(self):
        return "funktastic_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/funk_youtube_channels/funktastic_channel"
        super().__init__(root_path)

    def get_email(self):
        return "vidassetsmusic@gmail.com"