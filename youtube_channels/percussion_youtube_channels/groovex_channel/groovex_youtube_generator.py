from youtube_channels.percussion_youtube_channels.generic_percussion_youtube_generator import \
    GenericPercussionYoutubeGenerator


class GroovexYoutubeGenerator(GenericPercussionYoutubeGenerator):
    def get_pickle_name(self):
        return "groovex_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/percussion_youtube_channels/groovex_channel"
        super().__init__(root_path)

    def get_email(self):
        return "onymusicgroup@gmail.com"
