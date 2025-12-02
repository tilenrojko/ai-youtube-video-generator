from youtube_channels.hip_hop_youtube_channels.generic_hip_hop_youtube_generator import \
    GenericHipHopYoutubeGenerator


class HipHopHustleYoutubeGenerator(GenericHipHopYoutubeGenerator):
    def get_pickle_name(self):
        return "hip_hop_hustle_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/hip_hop_youtube_channels/hip_hop_hustle_channel"
        super().__init__(root_path)

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "90s rap wallpaper --v 6.0 --s 50 --style raw --ar 16:9"
