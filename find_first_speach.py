import speech_recognition as sr
from os import path
from pydub import AudioSegment

import time
# # convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\Screen_audio.wav"
# AUDIO_FILE = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\youre-so-funny-1.wav"
# AUDIO_FILE = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\file_example_WAV_1MG.wav"

s = time.time()


# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))

print(time.time() - s)
        
        
# ffmpeg -i "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen.mkv" -acodec pcm_s16le -ac 2 "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\Screen_audio.wav"