import file_system_utils as fsu

import subprocess
from turtle import done
import os.path



def convert_vid_file_to_mp4(in_path, out_path):
    cmd = 'HandBrakeCLI --input ' + in_path + '  --output ' + out_path 
    subprocess.call(cmd, shell=True)
    
    
# given the path to a dir with both vid files and non-vid files, will create a copy
# of that dir with all the vids converted to mp4s
def create_mp4_converted_copy_of_dir(in_dir_path, out_parent_dir_path):
    if fsu.is_dir(in_dir_path) != True:
        raise Exception("ERROR:  in_dir_path must point to dir")
    if fsu.get_parent_dir_from_path(in_path) == out_parent_dir_path:
        raise Exception("ERROR:  out_parent_dir_path cannot be the parent dir of in_dir_path")    
    
    # make new empty dir
    in_path_basename = fsu.get_basename_from_path(in_dir_path)
    new_dir_path = out_parent_dir_path + '//' + in_path_basename
    fsu.make_dir_if_not_exist(new_dir_path)
    
    # copy all files to new dir and recursivly run this function on all contained dirs
    obj_path_l = fsu.get_abs_path_l_of_all_objects_in_dir(in_dir_path)
    
    for obj_path in obj_path_l:
        if fsu.is_file(obj_path):
            fsu.copy_object_to_dest(obj_path, new_dir_path)
        elif fsu.is_dir(obj_path):
            create_mp4_converted_copy_of_dir(obj_path, new_dir_path)
        else:
            raise Exception("ERROR:  obj_path must be a file or a dir")
            
    
    
    
    
    
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




