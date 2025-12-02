from youtube_channels.hip_hop_youtube_channels.generic_hip_hop_youtube_generator import \
    GenericHipHopYoutubeGenerator


class HoppyYoutubeGenerator(GenericHipHopYoutubeGenerator):
    def get_pickle_name(self):
        return "hoppy_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/hip_hop_youtube_channels/hip_hop_hoppy_channel"
        super().__init__(root_path)

    def get_email(self):
        return "onymusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "illustration, in the style of hip hop aesthetics --v 6.0 --s 50 --style raw --ar 16:9"
