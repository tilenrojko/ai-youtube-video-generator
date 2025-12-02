from youtube_channels.rock_youtube_channels.generic_rock_youtube_generator import \
    GenericRockYoutubeGenerator


class TrashtideYoutubeGenerator(GenericRockYoutubeGenerator):
    def get_pickle_name(self):
        return "trashtide_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/rock_youtube_channels/trashtide_channel"
        super().__init__(root_path)

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "racing wallpaper, set against a uniquely cool and realistic backdrop. --ar 16:9 --v 6.0 --s 50 --style raw"
