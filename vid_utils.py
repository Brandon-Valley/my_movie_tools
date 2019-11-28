import subprocess

VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

#  --start-time=150 "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\transfer_dir\\Atonement_(720).m4v"




def open_vid(in_vid_path, start_time = 0):
    cmd = VLC_PATH + ' --start-time=' + str(start_time) + ' ' + in_vid_path
    print(cmd)
    subprocess.call(cmd, shell = False)
    
    
    
    
if __name__ == '__main__':
    open_vid("C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\transfer_dir\\Atonement_(720).m4v", 140)