import subprocess



'''returns .wav file, no spaces in path'''
def get_audio_from_video(in_vid_path, out_audio_path):
    cmd = 'ffmpeg -i ' + in_vid_path + ' -acodec pcm_s16le -ac 2 ' + out_audio_path
    subprocess.call(cmd, shell = True)
    
'''takes .wav file, no spaces in path'''    
def get_audio_duration(in_audio_path):
    cmd = 'ffprobe -i ' + in_audio_path + ' -show_entries format=duration -v quiet -of csv="p=0"'
    d = subprocess.check_output(cmd, shell = True)
    return float(d)




# ffprobe -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_trimmed.wav" -show_entries format=duration -v quiet -of csv="p=0"


if __name__ == '__main__':
    print(get_audio_duration("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\Screen_trimmed.wav"))
