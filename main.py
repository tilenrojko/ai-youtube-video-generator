import asyncio
import os
import shutil
from os import walk
from PIL import Image, ImageEnhance
import time
import datetime
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from midjourney_automation_script import generate_midjourney_prompt
from youtube_channels.cinematic_youtube_channels.cinematic_trailermaxx_channel.trailermaxx_youtube_generator import \
    TrailermaxxYoutubeGenerator
from youtube_channels.cinematic_youtube_channels.cinematix_channel.cinematix_youtube_generator import \
    CinematixYoutubeGenerator
from youtube_channels.corporate_youtube_channels.cskyline_channel.cskyline_youtube_generator import \
    CSkylineYoutubeGenerator
from youtube_channels.corporate_youtube_channels.pulsepro_channel.pulsepro_youtube_generator import \
    PulseproYoutubeGenerator
from youtube_channels.corporate_youtube_channels.strivecorp_channel.strivecorp_youtube_generator import \
    StriveCorpYoutubeGenerator
from youtube_channels.electronic_youtube_channels.dreamscape_youtube_generator.dreamscape_youtube_generator import \
    DreamScapeYoutubeGenerator
from youtube_channels.electronic_youtube_channels.neofrequency_youtube_generator.neonfrequency_youtube_generator import \
    NeonfrequencyYoutubeGenerator
from youtube_channels.electronic_youtube_channels.zolex_youtube_generator.zolex_youtube_generator import \
    ZolexYoutubeGenerator
from youtube_channels.funk_youtube_channels.boogie_wonderland_channel.boogie_wonderland_youtube_generator import \
    BoogieWonderlandYoutubeGenerator
from youtube_channels.funk_youtube_channels.funktastic_channel.funktastic_youtube_generator import \
    FunktasticYoutubeGenerator
from youtube_channels.funk_youtube_channels.townjam_channel.townjam_youtube_generator import \
    TownjamYoutubeGenerator
from youtube_channels.hip_hop_youtube_channels.hip_hop_flowmasters_channel.flowmasters_youtube_generator import \
    FlowmastersYoutubeGenerator
from youtube_channels.hip_hop_youtube_channels.hip_hop_hoppy_channel.hoppy_youtube_generator import \
    HoppyYoutubeGenerator
from youtube_channels.hip_hop_youtube_channels.hip_hop_hustle_channel.hip_hop_hustle_youtube_generator import \
    HipHopHustleYoutubeGenerator
from youtube_channels.lofi_youtube_channels.latte_channel.latte_youtube_generator import \
    LatteYoutubeGenerator
from youtube_channels.lofi_youtube_channels.lofi_chill_cafe_vibes_channel.chill_cafe_vibes_youtube_generator import \
    ChillCafeVibesYoutubeGenerator
from youtube_channels.lofi_youtube_channels.lofi_goodbeatz_channel.goodbeatz_youtube_generator import \
    GoodbeatzYoutubeGenerator
from youtube_channels.percussion_youtube_channels.drumsphere_channel.drumsphere_youtube_generator import \
    DrumsphereYoutubeGenerator
from youtube_channels.percussion_youtube_channels.groovex_channel.groovex_youtube_generator import \
    GroovexYoutubeGenerator
from youtube_channels.percussion_youtube_channels.rhythm_riot_channel.rhythm_riot_youtube_generator import \
    RhythmRiotYoutubeGenerator
from youtube_channels.pop_youtube_channels.pop_lolly_channel.pop_lolly_youtube_generator import \
    PopLollyYoutubeGenerator
from youtube_channels.pop_youtube_channels.pop_soundsway_channel.pop_soundsway_youtube_generator import \
    PopSoundswayYoutubeGenerator
from youtube_channels.pop_youtube_channels.pop_sunshine_melodies_channel.pop_sunshine_melodies_youtube_generator import \
    SunshineMelodiesYoutubeGenerator
from youtube_channels.rock_youtube_channels.furys_anthem_channel.furys_anthem_youtube_generator import \
    FurysAnthemYoutubeGenerator
from youtube_channels.rock_youtube_channels.trashtide_channel.trashtide_youtube_generator import \
    TrashtideYoutubeGenerator
from youtube_channels.rock_youtube_channels.unchained_channel.unchained_youtube_generator import \
    UnchainedYoutubeGenerator

RELEASED_MUSIC_FOLDER = "O:/VidAssets Music/Released Music"


def get_list_of_file_names(directory_path: str):
    f = []
    file_dict = {"dir": directory_path}
    print("Directory for saving : " + directory_path)
    for (dirpath, dirnames, filenames) in walk(directory_path + "/"):
        f.extend(filenames)
        break
    for directory_name in f:
        if ".jpg" in directory_name and "thumbnail" not in directory_name:
            file_dict["background"] = directory_path + "/" + directory_name
        possible_mp3_names = ["Long Version", "Main Version", "long version", "Full Version", "main version"]
        for mp3_name in possible_mp3_names:
            if mp3_name in directory_name \
                    and "compressed" not in directory_name \
                    and ".wav" not in directory_name \
                    and ".ogg" not in directory_name:
                file_dict["music"] = directory_path + "/" + directory_name
                break

    if file_dict.get("music") is None:
        raise Exception("No suitable MP3 file found.")
    file_dict_str = str(file_dict)

    print("Create file_dict: " + file_dict_str)

    return file_dict


def make_thumbnail(file_dir_dict, root_path):
    print("Making thumbnail for directory: " + file_dir_dict["background"])
    background = Image.open(file_dir_dict["background"])

    # Reduce brightness by 5%
    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.95)  # 5% darker

    text_overlay_path = root_path + "/text.png"

    foreground = Image.open(text_overlay_path)

    # Paste the foreground image
    background.paste(foreground, (0, 0), foreground)

    # Save the thumbnail

    thumbnail_path = file_dir_dict['dir'] + "/thumbnail.jpg"

    delete_path_if_exists(thumbnail_path)
    time.sleep(15)

    background.save(thumbnail_path)


def delete_path_if_exists(background_path):
    if os.path.exists(background_path):
        os.remove(background_path)


def calculate_next_upload_date(start_date):
    upload_days = ["Wednesday", "Friday", "Sunday"]
    day_name_to_num = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    upload_day_nums = [day_name_to_num[day] for day in upload_days]

    current_date = start_date
    while current_date.weekday() not in upload_day_nums:
        current_date += datetime.timedelta(days=1)

    return current_date


def make_youtube_n_desc_tags(generator, music_title):
    next_upload_date = calculate_next_upload_date(generator.upload_date)
    generator.set_upload_date(next_upload_date + datetime.timedelta(days=1))

    youtube_name = generator.get_youtube_video_name()
    tags = generator.get_youtube_tags()
    tags.append(youtube_name)

    print(tags)

    youtube_description = generator.create_youtube_description(music_title)

    request_body = {
        'snippet': {
            'categoryI': 10,
            'title': youtube_name,
            'description': youtube_description,
            'tags': tags
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': next_upload_date.isoformat() + "Z",
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': True
    }

    return request_body


def make_video(file_dir_dict):
    print("Making video")

    music_path = file_dir_dict["music"]

    thumbnail_path = os.path.join(file_dir_dict['dir'], "thumbnail.jpg")

    video_render_path = os.path.join(file_dir_dict["dir"], "render.mp4")

    render_path = video_render_path

    delete_path_if_exists(render_path)

    if not os.path.exists(music_path):
        raise FileNotFoundError(f"Music file not found: {music_path}")
    if not os.path.exists(thumbnail_path):
        raise FileNotFoundError(f"Thumbnail file not found: {thumbnail_path}")

    audio = AudioFileClip(music_path)
    clip = ImageClip(thumbnail_path).set_duration(audio.duration)
    clip = clip.set_audio(audio)
    clip.write_videofile(render_path, fps=30)

    print("Video created successfully")


def scale_images(weekly_upload_folders):
    for folder in weekly_upload_folders:
        print(folder)
        song_name = os.path.basename(folder)
        original_song_file_path = folder + "/" + song_name
        original_song_file_path_with_format = original_song_file_path + ".png"

        with open(original_song_file_path_with_format, 'rb') as image_file:
            image = Image.open(image_file)

            desired_size = (1920, 1080)
            resized_image = image.resize(desired_size, Image.LANCZOS)

            output_filename = original_song_file_path + "_resized.jpg"
            delete_path_if_exists(output_filename)

            print("original_song_file_path resized", output_filename)

            resized_image.save(output_filename, 'JPEG')

            image.close()


def extract_title_from_path(path):
    """
    Extracts a substring from the file path that is between the last backslash and the first opening parenthesis.

    :param path: The file path string.
    :return: The extracted substring.
    """
    # Find the position of the last backslash
    last_backslash = path.rfind('\\') + 1  # +1 to start after the backslash

    # Find the position of the first opening parenthesis
    first_parenthesis = path.find('(', last_backslash)

    # Extract and return the substring
    return path[last_backslash:first_parenthesis].strip()


async def main():
    time.sleep(5)
    sleep_time = 10

    cinematic_instances = await create_cinematic_generators(sleep_time)

    hip_hop_instances = await create_hip_hop_generators(sleep_time)

    funk_instances = await create_funk_instances(sleep_time)

    percussion_instances = await create_percussion_instances(sleep_time)

    corporate_instances = await create_corporate_instances(sleep_time)

    electronic_instances = await create_electronic_instances(sleep_time)

    lofi_instances = await create_lofi_generators(sleep_time)

    rock_instances = await create_rock_instances(sleep_time)

    pop_instances = await create_pop_instances(sleep_time)

    generator_lists = [
        cinematic_instances,
        hip_hop_instances,
        funk_instances,
        percussion_instances,
        corporate_instances,
        electronic_instances,
        lofi_instances,
        rock_instances,
        pop_instances
    ]

    for generator_list in generator_lists:
        i = 0
        for generator in generator_list:
            i += 1
            midjourney_prompt = generator.get_midjourney_prompt()
            subfolders = generator.get_subfolder_paths()

            await generate_midjourney_prompt(midjourney_prompt, subfolders)
            time.sleep(5)

            scale_images(subfolders)
            time.sleep(5)

            for music_folder in subfolders:
                print(
                    "\t\033[94mStarting upload process for folder: " + music_folder + " for generator: " + generator.get_pickle_name() + "\033[0m")

                file_directories = get_list_of_file_names(str(music_folder))
                make_thumbnail(file_directories, generator.root_path)
                make_video(file_directories)
                youtube_request_body = make_youtube_n_desc_tags(generator, extract_title_from_path(music_folder))
                generator.upload_video(youtube_request_body, music_folder)

                if i == len(generator_list):
                    move_folder_to_released(generator.get_genre())

                await asyncio.sleep(5)


def delete_thumbnails_from_subfolders(music_folder):
    thumbnail_path = music_folder + "/thumbnail.jpg"
    delete_path_if_exists(thumbnail_path)


async def create_lofi_generators(sleep_time):
    goodbeatz_instance = GoodbeatzYoutubeGenerator()
    time.sleep(sleep_time)

    lofi_caffe_vibes_instance = ChillCafeVibesYoutubeGenerator()
    time.sleep(sleep_time)

    latte_instance = LatteYoutubeGenerator()
    time.sleep(sleep_time)

    return [
        goodbeatz_instance,
        lofi_caffe_vibes_instance,
        latte_instance
    ]


async def create_cinematic_generators(sleep_time):
    cinematix_instance = CinematixYoutubeGenerator()
    time.sleep(sleep_time)

    trailermaxx_instance = TrailermaxxYoutubeGenerator()
    time.sleep(sleep_time)

    return [
        trailermaxx_instance,
        cinematix_instance
    ]


async def create_corporate_instances(sleep_time):
    cskyline_instance = CSkylineYoutubeGenerator()
    time.sleep(sleep_time)

    pulsepro_instance = PulseproYoutubeGenerator()
    time.sleep(sleep_time)

    strivecorp_instance = StriveCorpYoutubeGenerator()
    time.sleep(sleep_time)

    corporate_instances = [
        cskyline_instance,
        pulsepro_instance,
        strivecorp_instance
    ]
    return corporate_instances


async def create_electronic_instances(sleep_time):
    neon_frequency_instance = NeonfrequencyYoutubeGenerator()
    time.sleep(sleep_time)

    dreamscape_instance = DreamScapeYoutubeGenerator()
    time.sleep(sleep_time)

    zolex_instance = ZolexYoutubeGenerator()
    time.sleep(sleep_time)

    return [
        neon_frequency_instance,
        dreamscape_instance,
        zolex_instance
    ]


async def create_rock_instances(sleep_time):
    unchained_instance = UnchainedYoutubeGenerator()
    time.sleep(sleep_time)

    furys_anthem_instance = FurysAnthemYoutubeGenerator()
    time.sleep(sleep_time)

    trashtide_instance = TrashtideYoutubeGenerator()
    time.sleep(sleep_time)

    return [
        unchained_instance,
        furys_anthem_instance,
        trashtide_instance
    ]


async def create_percussion_instances(sleep_time):
    drumsphere_instance = DrumsphereYoutubeGenerator()
    time.sleep(sleep_time)

    groovex_instance = GroovexYoutubeGenerator()
    time.sleep(sleep_time)

    rhythmriot_instance = RhythmRiotYoutubeGenerator()
    time.sleep(sleep_time)

    percussion_instances = [
        drumsphere_instance,
        groovex_instance,
        rhythmriot_instance
    ]
    return percussion_instances


async def create_funk_instances(sleep_time):
    funktastic_instance = FunktasticYoutubeGenerator()
    time.sleep(sleep_time)

    boogie_wonderland_instance = BoogieWonderlandYoutubeGenerator()
    time.sleep(sleep_time)

    townjam_instance = TownjamYoutubeGenerator()
    time.sleep(sleep_time)

    funk_instances = [
        funktastic_instance,
        boogie_wonderland_instance,
        townjam_instance
    ]
    return funk_instances


async def create_hip_hop_generators(sleep_time):
    flowmasters_instance = FlowmastersYoutubeGenerator()
    time.sleep(sleep_time)

    hoppy_instance = HoppyYoutubeGenerator()
    time.sleep(sleep_time)

    hip_hop_hustle_instance = HipHopHustleYoutubeGenerator()
    time.sleep(sleep_time)

    hip_hop_instances = [
        flowmasters_instance,
        hoppy_instance,
        hip_hop_hustle_instance
    ]
    return hip_hop_instances


async def create_pop_instances(sleep_time):
    lolly_instance = PopLollyYoutubeGenerator()
    time.sleep(sleep_time)

    soundsway_instance = PopSoundswayYoutubeGenerator()
    time.sleep(sleep_time)

    sunshine_melodies_instance = SunshineMelodiesYoutubeGenerator()
    time.sleep(sleep_time)

    hip_hop_instances = [
        lolly_instance,
        soundsway_instance,
        sunshine_melodies_instance
    ]

    return hip_hop_instances


genre_mapping = {
    "abstract": "abstract",
    "christmas": "christmas",
    "cinematic": "cinematic",
    "corporate": "corporate",
    "electronic": "electronic",
    "synthwave": "synthwave",
    "future bass": "future bass",
    "funk": "funk",
    "retro": "retro",
    "lofi": "lofi",
    "hiphop": "hip hop",
    "percussion": "percussion",
    "pop": "pop",
    "rock": "rock",
    "trap": "trap",
    "aggressive": "electronic",
    "inspirational": "cinematic",
    "inspiring": "cinematic",
    "instagram": "electronic",
    "old school": "hip hop",
    "hip-hop": "hip hop",
    "techno": "electronic",
    "opener": "electronic"
}


def get_last_folder_name_using_os(path: str) -> str:
    return os.path.basename(os.path.normpath(path))


def move_folder_to_released(generator_name):
    directory_to_move = RELEASED_MUSIC_FOLDER
    folder_name = get_last_folder_name_using_os(generator_name)

    if os.path.isdir(generator_name):
        genre = None
        for key, value in genre_mapping.items():
            if key in generator_name.lower(): 
                genre = value
                break

        if genre:
            genre_dir = os.path.join(directory_to_move, genre)

            if not os.path.exists(genre_dir):
                os.makedirs(genre_dir)

            new_location = os.path.join(genre_dir, folder_name)
            if not os.path.exists(new_location):  # Check to avoid overwrite
                shutil.move(generator_name, new_location)
                print(f"Moved '{folder_name}' to '{genre_dir}'")
            else:
                print(f"Directory '{folder_name}' already exists in '{genre_dir}'")


if __name__ == "__main__":
    asyncio.run(main())
