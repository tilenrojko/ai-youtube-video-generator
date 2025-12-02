from youtube_channels.rock_youtube_channels.generic_rock_youtube_generator import \
    GenericRockYoutubeGenerator


class UnchainedYoutubeGenerator(GenericRockYoutubeGenerator):
    def get_pickle_name(self):
        return "unchained_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/rock_youtube_channels/unchained_channel"
        super().__init__(root_path)

    def get_email(self):
        return "onymusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "mad max wallpaper, set against a uniquely cool and realistic backdrop. --ar 16:9 --v 6.0 --s 50 --style raw"
