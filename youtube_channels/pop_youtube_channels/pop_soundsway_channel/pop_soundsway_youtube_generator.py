from youtube_channels.pop_youtube_channels.generic_pop_youtube_generator import \
    GenericPopYoutubeGenerator


class PopSoundswayYoutubeGenerator(GenericPopYoutubeGenerator):
    def get_pickle_name(self):
        return "soundsway_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/pop_youtube_channels/pop_soundsway_channel"
        super().__init__(root_path)

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"


    def get_midjourney_prompt(self):
        return "happy pop video still, in the style of real photography --v 6.0 --s 50 --style raw --ar 16:9"

