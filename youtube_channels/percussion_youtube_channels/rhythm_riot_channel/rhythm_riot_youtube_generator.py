from youtube_channels.percussion_youtube_channels.generic_percussion_youtube_generator import \
    GenericPercussionYoutubeGenerator


class RhythmRiotYoutubeGenerator(GenericPercussionYoutubeGenerator):
    def get_pickle_name(self):
        return "rhythm_riot_pickle"

    def __init__(self):
        root_path = "X:/PyCharm/youtube_bot/youtube_channels/percussion_youtube_channels/rhythm_riot_channel"
        super().__init__(root_path)

    def get_email(self):
        return "cinematixmusicgroup@gmail.com"

    def get_midjourney_prompt(self):
        return "sport activity, in the style of real photography --ar 16:9 --v 6.0 --s 50 --style raw"

