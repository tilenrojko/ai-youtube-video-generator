from youtube_channels.hip_hop_youtube_channels.generic_hip_hop_youtube_generator import \
    GenericHipHopYoutubeGenerator


class FlowmastersYoutubeGenerator(GenericHipHopYoutubeGenerator):
    def get_pickle_name(self):
        return "flowmasters_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/hip_hop_youtube_channels/hip_hop_flowmasters_channel"
        super().__init__(root_path)

    def get_email(self):
        return "vidassetsmusic@gmail.com"