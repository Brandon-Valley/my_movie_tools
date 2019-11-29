import subprocess

import file_system_utils as fsu
from macgyyver_stuff import episode_lists


MKVToolNix_PATH = "C:\\Program Files (x86)\\MKVToolNix\\mkvpropedit"
DVD_RIP_DIR_PATH = "F:\\Movies_and_TV\\Movies\\___DVD_RIP"


# TEST_PATH = "C:\\Video\\Screen Test- Dance Instructor.mkv"
# TEST_PATH = "C:\\Video\\The Hunger Games_t00.mkv"


# NEW_FILE_NAME = 'The Hunger Games 1.mkv'
# NEW_FILE_NAME = 'Star Wars 3 - The Revenge of the Sith.mkv'
NEW_FILE_NAME = 'Peter Pan 2 - Return to Never Land.mkv'
# NEW_FILE_NAME = 'The Lord of the Rings 2 - The Two Towers.mkv'

# SE_L = episode_lists.SE_L
FIRST_EPISODE_NUM = 9
# NUM_EPISODES = 4
SEASON_NUM = 1


    
EPISODE_MODE = True







def rename_and_move_file_to_final_dest(in_vid_path, new_vid_name, dest_path):
    final_vid_path = dest_path + '\\' + new_vid_name
    
    if fsu.is_file(final_vid_path):
        raise Exception(new_vid_name + " already exists in DVD_RIP_DIR")
    
    parent_dir_path = fsu.get_parent_dir_from_path(in_vid_path)
    new_vid_path = parent_dir_path + '\\' + new_vid_name
    
    
    
    fsu.rename_file_overwrite(in_vid_path, new_vid_path)
    print('copying ' , new_vid_path, ' to ', dest_path, '...')
    fsu.copy_files_to_dest([new_vid_path], dest_path)
    fsu.delete_if_exists(new_vid_path)
    
    
    
def disable_mkv_default_subtitles(in_vid_path):
    cmd = '"' +  MKVToolNix_PATH + '" "' + in_vid_path + '" --edit track:s1 --set flag-default=0' 
    subprocess.call(cmd)









# mkvpropedit movie.mkv --edit track:s1 --set flag-default=0
# mkvpropedit "C:\\Video\\Screen Test- Dance Instructor.mkv" --edit track:s1 --set flag-default=0
# 


if EPISODE_MODE:
    START_DIR_PATH = "C:\\Video\\a"
    abs_path_l = fsu.get_file_paths_in_dir_by_age(START_DIR_PATH)
    
    
    dest_dir_name = 'MacGyver\\MacGyver - Season ' + str(SEASON_NUM)
    
    
    episode_name_l = []
    
    for x in range(len(abs_path_l)):
        e_num = FIRST_EPISODE_NUM + x
        file_name = "MacGyver - S" + str(SEASON_NUM) + " E" + str(e_num) + " - " + episode_lists.SE_L[SEASON_NUM - 1][e_num - 1] + '.mkv'
        print(file_name)
        episode_name_l.append(file_name)
        print(episode_name_l)
    
    
    
#     episode_name_l = ["MacGyver - S1 E" + str(FIRST_EPISODE_NUM    ) + " - Pilot",
#                   "MacGyver - S1 E" + str(FIRST_EPISODE_NUM + 1) + " - The Golden Triangle",
#                   "MacGyver - S1 E" + str(FIRST_EPISODE_NUM + 2) + " - Thief of Budapest",
#                   "MacGyver - S1 E" + str(FIRST_EPISODE_NUM + 3) + " - The Gauntlet"]
    
    
    
    
    
    for path_num, og_vid_path in enumerate(reversed(abs_path_l)):
        disable_mkv_default_subtitles(og_vid_path)
        rename_and_move_file_to_final_dest(og_vid_path, episode_name_l[path_num], DVD_RIP_DIR_PATH + '\\' + dest_dir_name)
else:
    START_DIR_PATH = "C:\\Video"
    abs_path_l = fsu.get_file_paths_in_dir_by_age(START_DIR_PATH)

    og_vid_path = abs_path_l[0]
    
    disable_mkv_default_subtitles(og_vid_path)
    rename_and_move_file_to_final_dest(og_vid_path, NEW_FILE_NAME, DVD_RIP_DIR_PATH)
print('done!')


# ffmpeg -i "C:\Users\Brandon\Downloads\messages_0.3gpp" -vf "transpose=2" "C:\Users\Brandon\Documents\Personal_Projects\my_movie_tools_big_data\messages_0.3gpp.mp4"




