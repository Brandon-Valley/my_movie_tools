import audio_edit_utils
import vid_utils


# "C:\Program Files\VideoLAN\VLC\vlc.exe" --start-time=35 "C:\Users\Brandon\AppData\Roaming\I2P\i2psnark\Rick.and.Morty.S04E03.720p.WEBRip.x264-TBS[rarbg]\rick.and.morty.s04e03.720p.webrip.x264-tbs.mkv"
# "C:\Program Files\VideoLAN\VLC\vlc.exe" --start-time=150 "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\transfer_dir\\Atonement_(720).m4v"


# import speech_recognition as sr
# from os import path
# from pydub import AudioSegment


#     if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError()
# speech_recognition.UnknownValueError


import time








# VID_FILE_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\dolbycanyon_outside.mkv"
# VID_FILE_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\transfer_dir\\Atonement_(720).m4v"
VID_FILE_PATH = "C:/tmp/S10E05__Family_Guy__Back_To_The_Pilot__Clip____TBS.mkv"
# VID_FILE_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\Screen.mkv"

FULL_AUDIO_PATH   = '..\\my_movie_tools_big_data\\full_audio.wav'
CLIPED_AUDIO_PATH = '..\\my_movie_tools_big_data\\clipped_audio.wav'
AUDIO_CLIP_TIME = 10 # number of seconds to divide audio into to check for speech





# returns # of seconds after start_time before the first time someone speaks in the audio (.wav file)
# returns False if there is no speech in audio clip
def get_first_speech_time(full_audio_path, start_time):
    audio_duration = audio_edit_utils.get_audio_duration(full_audio_path)
    cur_time = start_time
    keep_looping = True
    
    while(keep_looping):
        # get end time for clipping audio
        end_time = cur_time + AUDIO_CLIP_TIME
        if end_time > audio_duration:
            end_time = audio_duration
            keep_looping = False
            
        # clip audio
        audio_edit_utils.clip_audio(full_audio_path, CLIPED_AUDIO_PATH, cur_time, end_time)
        
        # transcribe audio
        transcription = audio_edit_utils.transcribe_audio(CLIPED_AUDIO_PATH)

        # return time if speech was found in audio clip
        if transcription != False:
            return cur_time
    
        # set up for next loop if no speech was found in audio clip
        cur_time = end_time
    return False











# extract audio from vid
audio_edit_utils.get_audio_from_video(VID_FILE_PATH, FULL_AUDIO_PATH)

first_speech_time = get_first_speech_time(FULL_AUDIO_PATH, 0)

print(first_speech_time)




# 
# 
# 
# # # convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\ste-021-dilan-herkunft.mp3")
# sound.export("transcript.wav", format="wav")
# 
# 
# # transcribe audio file                                                         
# AUDIO_FILE = "transcript.wav"
# # AUDIO_FILE = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\Screen_audio.wav"
# # AUDIO_FILE = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\youre-so-funny-1.wav"
# # AUDIO_FILE = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\file_example_WAV_1MG.wav"
# 
# s = time.time()
# 
# 
# # use the audio file as the audio source                                        
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)  # read the entire audio file                  
# 
#         print("Transcription: " + r.recognize_google(audio))
# 
# print(time.time() - s)
#         
# # ffmpeg -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_audio.wav" -ss 10 -to 15 -c copy "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_audio_10-15.wav"
# #         
# #         
# #         
# # ffmpeg -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_trimmed.mp4" -acodec pcm_s16le -ac 2 "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_trimmed.wav"
# # # ffmpeg -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen.mkv" -acodec pcm_s16le -ac 2 "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_audio.wav"
# # ffmpeg -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_trimmed.wav" 2>&1 | grep Duration | sed 's/Duration: \(.*\), start/\1/g'
# # ffprobe -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_trimmed.wav" -show_entries format=duration -v quiet -of csv="p=0"







