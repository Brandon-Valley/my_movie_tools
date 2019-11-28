import subprocess

import file_system_utils as fsu

MKVToolNix_PATH = "C:\\Program Files (x86)\\MKVToolNix\\mkvpropedit"
DVD_RIP_DIR_PATH = "F:\\Movies_and_TV\\Movies\\___DVD_RIP"
START_DIR_PATH = "C:\\Video"

TEST_PATH = "C:\\Video\\Screen Test- Dance Instructor.mkv"
# TEST_PATH = "C:\\Video\\The Hunger Games_t00.mkv"


NEW_FILE_NAME = 'The Hunger Games 1.mkv'




def rename_and_move_file_to_final_dest(in_vid_path):
    final_vid_path = DVD_RIP_DIR_PATH + '\\' + NEW_FILE_NAME
    
    if fsu.is_file(final_vid_path):
        raise Exception(NEW_FILE_NAME + " already exists in DVD_RIP_DIR")
    
    parent_dir_path = fsu.get_parent_dir_from_path(in_vid_path)
    new_vid_path = parent_dir_path + '\\' + NEW_FILE_NAME
    
    
    
    fsu.rename_file_overwrite(in_vid_path, new_vid_path)
    print('copying ' , new_vid_path, ' to ', DVD_RIP_DIR_PATH, '...')
    fsu.copy_files_to_dest([new_vid_path], DVD_RIP_DIR_PATH)
    fsu.delete_if_exists(in_vid_path)
    
    
    
def disable_mkv_default_subtitles(in_vid_path):
    cmd = '"' +  MKVToolNix_PATH + '" "' + in_vid_path + '" --edit track:s1 --set flag-default=0' 
    print(cmd)
    subprocess.call(cmd)

# mkvpropedit movie.mkv --edit track:s1 --set flag-default=0
# mkvpropedit "C:\\Video\\Screen Test- Dance Instructor.mkv" --edit track:s1 --set flag-default=0
# 
abs_path_l = fsu.get_file_paths_in_dir_by_age(START_DIR_PATH)
og_vid_path = abs_path_l[0]
# print(abs_path_l)


# move_file_to_final_dest(abs_path_l[0])

disable_mkv_default_subtitles(og_vid_path)
rename_and_move_file_to_final_dest(og_vid_path)







