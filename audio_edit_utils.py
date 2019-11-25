import subprocess
import speech_recognition as sr
from os import path
from pydub import AudioSegment


'''returns .wav file, no spaces in path, will overwrite'''
def get_audio_from_video(in_vid_path, out_audio_path):
    cmd = 'ffmpeg -i ' + in_vid_path + ' -acodec pcm_s16le -ac 2 ' + out_audio_path + ' -y'
    subprocess.call(cmd, shell = False)
    
    
'''takes .wav file, no spaces in path'''    
def get_audio_duration(in_audio_path):
    cmd = 'ffprobe -i ' + in_audio_path + ' -show_entries format=duration -v quiet -of csv="p=0"'
    d = subprocess.check_output(cmd, shell = False)
    return float(d)


'''takes .wav file, no spaces in path, will overwrite'''
def clip_audio(in_audio_path, cliped_audio_path, start_time, end_time):
    cmd = 'ffmpeg -i ' + in_audio_path + ' -ss ' + str(start_time) + ' -to ' + str(end_time) + ' -c copy ' + cliped_audio_path + ' -y'
    subprocess.call(cmd, shell = False)


# returns False if there is no speach in audio
def transcribe_audio(in_audio_path):
    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(in_audio_path) as source:
            audio = r.record(source)  # read the entire audio file                  
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return False





# ffprobe -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_trimmed.wav" -show_entries format=duration -v quiet -of csv="p=0"


if __name__ == '__main__':
#     print(get_audio_duration("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\Screen_trimmed.wav"))
    print(transcribe_audio("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools\\clipped_audio.wav"))
