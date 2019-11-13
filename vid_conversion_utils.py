import file_system_utils

import subprocess
from turtle import done
import os.path



def convert_vid_file_to_mp4(in_path, out_path):
    cmd = 'HandBrakeCLI --input ' + in_path + '  --output ' + out_path 
    subprocess.call(cmd, shell=True)
    
    
# given the path to a dir with both vid files and non-vid files, will create a copy
# of that dir with all the vids converted to mp4s
def create_mp4_converted_copy_of_dir(in_path, out_parent_dir_path):
    if file_system_utils.is_dir(in_path) != True:
        raise Exception("ERROR:  in_path must point to dir")
    if file_system_utils.get_parent_dir_from_path(in_path) == out_parent_dir_path:
        raise Exception("ERROR:  out_parent_dir_path cannot be the parent dir of in_path")    
    
    
    in_path_basename = file_system_utils.get_basename_from_path(in_path)
    new_root_dir_path = out_parent_dir_path + '//' + in_path_basename
    
#     print(new_root_dir_path)
    file_system_utils.make_dir_if_not_exist(new_root_dir_path)
    
    
    
    
    
in_path             = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids"
out_parent_dir_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\out_dir"
    
# create_mp4_converted_copy_of_dir('sdnfondso', 'sdnf')    
create_mp4_converted_copy_of_dir(in_path, out_parent_dir_path)

# 
# test_vid_1_path = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Instructor.mkv'
# test_out_path   = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Instructor.mp4'
# test_out_path   = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Instructor2.mp4'
# # test_out_path   = 'Instructor.mp4"'
# # test_out_path   = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids\\Screen Test- Dance Instructor.mp4"
# 
# # cmd = 'HandBrakeCLI --input ' + test_vid_1_path + ' --title 0 --preset Normal --output ' + test_out_path
# # cmd = 'HandBrakeCLI --input ' + test_vid_1_path + ' --title 0 --preset Normal --output ' + test_out_path
# # cmd = 'HandBrakeCLI --input ' + test_vid_1_path + ' --preset Normal --output ' + test_out_path
# # cmd = 'HandBrakeCLI --input ' + test_vid_1_path + '  --output ' + test_out_path 
# # print(cmd)
# # 
# # subprocess.call(cmd, shell=True) ; done
# 
# convert_vid_file_to_mp4(test_vid_1_path, test_out_path) ; done
# 
# for x in range (10):
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# 
# 
# 
# cmd = 'HandBrakeCLI --input ' + test_vid_1_path + '  --output ' + test_out_path2 



