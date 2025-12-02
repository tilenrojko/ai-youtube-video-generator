from youtube_channels.rock_youtube_channels.generic_rock_youtube_generator import \
    GenericRockYoutubeGenerator


class FurysAnthemYoutubeGenerator(GenericRockYoutubeGenerator):
    def get_pickle_name(self):
        return "furys_anthem_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/rock_youtube_channels/furys_anthem_channel"
        super().__init__(root_path)

    def get_email(self):
        return "vidassetsmusic@gmail.com"

    def get_midjourney_prompt(self):
        return "extreme manly sports wallpaper, set against a uniquely cool and realistic backdrop. --ar 16:9 --v 6.0 --s 50 --style raw"
