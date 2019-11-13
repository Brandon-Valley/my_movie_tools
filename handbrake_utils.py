import subprocess
from turtle import done

test_vid_1_path = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Instructor.mkv'
test_out_path   = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Instructor.mp4'
test_out_path   = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Instructor2.mp4'
# test_out_path   = 'Instructor.mp4"'
# test_out_path   = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Screen Test- Dance Instructor.mp4"

# cmd = 'HandBrakeCLI --input ' + test_vid_1_path + ' --title 0 --preset Normal --output ' + test_out_path
# cmd = 'HandBrakeCLI --input ' + test_vid_1_path + ' --title 0 --preset Normal --output ' + test_out_path
# cmd = 'HandBrakeCLI --input ' + test_vid_1_path + ' --preset Normal --output ' + test_out_path
cmd = 'HandBrakeCLI --input ' + test_vid_1_path + '  --output ' + test_out_path 
print(cmd)

subprocess.call(cmd, shell=True) ; done

for x in range (10):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



cmd = 'HandBrakeCLI --input ' + test_vid_1_path + '  --output ' + test_out_path2 




