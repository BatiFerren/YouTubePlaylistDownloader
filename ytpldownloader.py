from pytube import Playlist
import os
from sys import argv


def replacing_dots(start_string):
    char_list = []
    for character in start_string:
        if character == '.' or character == ',' or character == '?' or character == ':' or character == '|' or character == '/':
            character = ''
        char_list.append(character)
    res_str = ''.join(char_list)
    return res_str


def create_directory(base_path, playlist):
    dir_name = playlist.title
    end_dir = replacing_dots(dir_name)
    path = os.path.join(base_path, end_dir)
    try:
        os.mkdir(path)
        print("Directory {} has been created.".format(playlist.title))
    except OSError as error:
        print(error)
    return path


def main():
    try:
        script, url = argv
    except ValueError:
        print("You have no entered the URL of playlist")
        return 1
    p = Playlist(url)
    base_path = '/put/path/to/download/directory/here'
    out_path = create_directory(base_path, p)
    videos_list = p.videos
    count_file = 0
    for video in videos_list:
        count_file += 1
        video_obj = video.streams.filter(progressive=True).last()
        file_name = str(count_file) + ' ' + replacing_dots(video_obj.title)
        try:
            video_obj.download(output_path=out_path, filename=file_name)
            print('{} - has been downloaded'.format(file_name))
        except OSError as error:
            print(error)
    print('<=========Playlist has been downloaded=========>')


if __name__ == "__main__":
    main()
