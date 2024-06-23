
from pathlib import Path
from sms.file_system_utils import file_system_utils as fsu
import subprocess

import os
import time

SCRIPT_PARENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def delete_all_metadata_from_all_mp4_in_dir(in_dir_path):
    abs_path_l = fsu.get_dir_content_l(in_dir_path, 'file', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)
    
    for abs_path in abs_path_l:
        if fsu.get_extention(abs_path) == '.wzmp4' and os.path.basename(abs_path)[0] not in '1234567890 abcde': # 2nd part temp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            temp_no_metadata_file_abs_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'temp.mp4')

            Path(temp_no_metadata_file_abs_path).parent.mkdir(parents=True, exist_ok=True)
            
            # delete temp file from previous test if exists
            fsu.delete_if_exists(temp_no_metadata_file_abs_path)
            
            # make temp file with deleted metadata
            cmd = 'ffmpeg -i "{}" -map_metadata "-1" -c:v copy -c:a copy "{}"'.format(abs_path, temp_no_metadata_file_abs_path)
            print("Running {}...".format(cmd))
            subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # subprocess.call(cmd, shell=True)
            print("Done running ffmpeg")
            assert Path(temp_no_metadata_file_abs_path).is_file()

            # delete og file
            fsu.delete_if_exists(abs_path)
            
            time.sleep(1)
             
            # rename temp file to og name
            fsu.rename_file_overwrite(temp_no_metadata_file_abs_path, abs_path)
            
            
def delete_all_metadata_from_all_mp4_in_movie_dirs(movies_dir_path):
    '''
        Given dir that contains movie dirs (dir that contains movie mp4 file),
        goes into each movie dir and removes metadata from all contained mp4s
    '''
            
    # abs_path_l = fsu.get_dir_content_l(movies_dir_path, 'dir', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)

    abs_path_l = []
    for path_obj in Path(movies_dir_path).glob("*"):
        if path_obj.is_dir():
            abs_path_l.append(path_obj.as_posix())
    
    for abs_path in abs_path_l:
        print(abs_path)
        delete_all_metadata_from_all_mp4_in_dir(abs_path)


if __name__ == "__main__":
    
#     untested main
    
    # MOVIES_DIR_PATH = 'F:\\Movies'
    # MOVIES_DIR_PATH = 'D:\\Movies_and_TV\\Movies\\The Witches (2020)'
    MOVIES_DIR_PATH = 'C:\\vuze_downloads\\completed'
    


    delete_all_metadata_from_all_mp4_in_movie_dirs(MOVIES_DIR_PATH)
    print('done')
    
    
    
    
    
    
    
    