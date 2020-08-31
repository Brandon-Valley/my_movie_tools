# https://lifehacker.com/set-up-a-fully-automated-torrent-seeding-media-center-5595586

import file_system_utils as fsu

import subprocess
from turtle import done
import os.path

VID_FILE_TYPES_TO_BE_CONVERTED = ['.avi', '.mkv']
MKVToolNix_PATH = "C:\\Program Files (x86)\\MKVToolNix\\mkvpropedit"



def disable_mkv_default_subtitles(in_vid_path):
    cmd = '"' +  MKVToolNix_PATH + '" "' + in_vid_path + '" --edit track:s1 --set flag-default=0' 
    subprocess.call(cmd)



''' no subtitles '''
def convert_vid_file_to_mp4(in_path, dest_parent_dir_path):
    print(' converting ', in_path, " to inside of ", dest_parent_dir_path)#````````````````````````````````````````````````````````````
    
    in_basename = fsu.get_basename_from_path(in_path)
    out_basename = fsu.replace_extension(in_basename, 'mp4')
    dest_path = dest_parent_dir_path + '//' + out_basename
    
    cmd = 'HandBrakeCLI --input "' + in_path + '"  --output "' + dest_path + '"'
    subprocess.call(cmd, shell=True)
    
    
    
def convert_vid_file_to_mkv(in_path, dest_parent_dir_path):
    print(' converting ', in_path, " to inside of ", dest_parent_dir_path)#````````````````````````````````````````````````````````````
    
    in_basename = fsu.get_basename_from_path(in_path)
    out_basename = fsu.replace_extension(in_basename, 'mkv')
    dest_path = dest_parent_dir_path + '//' + out_basename
    
    cmd = 'HandBrakeCLI --input "' + in_path + '"  --output "' + dest_path + '" --all-subtitles'
    subprocess.call(cmd, shell=True)
    
    
    
    
# given the path to a dir with both vid files and non-vid files, will create a copy
# of that dir with all the vids converted to new file type
# also disables subs for mkv files
def create_vid_converted_copy_of_dir(in_dir_path, dest_parent_dir_path, new_vid_type = 'mkv', delete_og = False):
    if fsu.is_dir(in_dir_path) != True:
        raise Exception("ERROR:  in_dir_path must point to dir")
    if fsu.get_parent_dir_from_path(in_dir_path) == dest_parent_dir_path:
        raise Exception("ERROR:  dest_parent_dir_path cannot be the parent dir of in_dir_path")    
    
    # make new empty dir
    in_path_basename = fsu.get_basename_from_path(in_dir_path)
    new_dir_path = dest_parent_dir_path + '//' + in_path_basename
    fsu.make_dir_if_not_exist(new_dir_path)
    
    
    # copy all files to new dir and recursively run this function on all contained dirs
    obj_path_l = fsu.get_abs_path_l_of_all_objects_in_dir(in_dir_path)
    print('obj_path_l:  ', obj_path_l)#`````````````````````````````````````````````````````````````````````````````
    
    for obj_path in obj_path_l:
        if fsu.is_file(obj_path):
            # convert vid files, copy over other files            
            if fsu.get_file_extension(obj_path) in VID_FILE_TYPES_TO_BE_CONVERTED:
                if new_vid_type == 'mkv':
                    convert_vid_file_to_mkv(obj_path, new_dir_path)
                elif new_vid_type == 'mp4':
                    raise Exception("ERROR:  convert to mp4 will make you loose subs, and other stuff not set up for it, comment this out to continue")
                    convert_vid_file_to_mp4(obj_path, new_dir_path)
                else:
                    raise Exception("ERROR:  Invalid new_vid_type: ", new_vid_type)
                
                if delete_og:
                    fsu.delete_if_exists(obj_path)

            else:
                fsu.copy_object_to_dest(obj_path, new_dir_path)
            
        elif fsu.is_dir(obj_path):
            create_vid_converted_copy_of_dir(obj_path, new_dir_path)
        else:
            raise Exception("ERROR:  obj_path must be a file or a dir")
            



# converts and transfers dir or vid file to dest dir
def convert_and_transfer(in_path, dest_parent_dir_path):
    if fsu.is_dir(in_path):
        create_vid_converted_copy_of_dir(in_path, dest_parent_dir_path)
    elif fsu.is_file(in_path):
        if fsu.get_file_extension(in_path) in VID_FILE_TYPES_TO_BE_CONVERTED:
            convert_vid_file_to_mp4(in_path, dest_parent_dir_path)
        else:
            fsu.copy_object_to_dest(in_path, dest_parent_dir_path)
    
    
    
def convert_and_transfer_objects_from_path_l(in_path_l, dest_parent_dir_path):
    for path in in_path_l:
        convert_and_transfer(path, dest_parent_dir_path)
    
    
    
# # in_path              = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\test_vids"
# dest_parent_dir_path = "F:\\Photos\\2019\\Birthdays\\Birthday - Sue Valley (2019)\\Videos\\MP4 Files"
# # dest_parent_dir_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\out_dir"
# # outside_mkv_path     = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\dolbycanyon_outside.mkv"
# path_l = ["F:\\Photos\\2019\\Birthdays\\Birthday - Sue Valley (2019)\\Videos\\.MOV Files",
#           ]
#     
#     
# # convert_and_transfer_objects_from_path_l(path_l, dest_parent_dir_path)
#     
#     
# og = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\transfer_dir\\MacGyver - S1 E1 - Pilot.mkv"
# new_p_dir = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\my_movie_tools_big_data\\transfer_dir\\zzz_to_convert"
# # convert_vid_file_to_mkv(og, new_p_dir)
# 
# disable_mkv_default_subtitles(og)


in_dir_path = "D:\\Movies_and_TV\\Movies\\___DVD_RIP"
dest_parent_dir_path = "D:\\Movies_and_TV\\Movies\\__DVD_RIP_AFTER_CONVERT"

create_vid_converted_copy_of_dir(in_dir_path, dest_parent_dir_path, new_vid_type = 'mkv', delete_og = True)




    
# mkvpropedit options "F:\Movies_and_TV\Movies\___DVD_RIP\Wreck-It Ralph [720p].mkv" -l
# mkvpropedit "F:\Movies_and_TV\Movies\___DVD_RIP\Wreck-It Ralph [720p].mkv" -l



