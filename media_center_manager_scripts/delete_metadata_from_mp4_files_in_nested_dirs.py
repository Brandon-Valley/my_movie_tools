
from sms.file_system_utils import file_system_utils as fsu
from sms.subprocess_utils  import subprocess_utils  as su

import os
import time

MOVIES_DIR_PATH = 'F:\\Movies'
PWD = os.path.dirname(os.path.abspath(__file__))



def delete_all_metadata_from_all_mp4_in_dir(in_dir_path):
    abs_path_l = fsu.get_dir_content_l(in_dir_path, 'file', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)
    
    for abs_path in abs_path_l:
        if fsu.get_extention(abs_path) == '.mp4' and os.path.basename(abs_path)[0] not in '1234567890 abcde': # 2nd part temp!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            temp_no_metadata_file_abs_path = PWD + '//temp.mp4'           
            
            # delete temp file from previous test if exists
            fsu.delete_if_exists(temp_no_metadata_file_abs_path)
            
            # make temp file with deleted metadata
            cmd = 'ffmpeg -i "{}" -map_metadata "-1" -c:v copy -c:a copy "{}"'.format(abs_path, temp_no_metadata_file_abs_path)
            su.run_cmd_popen(cmd, print_output = False, print_cmd = True)#, shell = False, decode = False, strip = False, always_output_list = False, return_stderr = True)
#             subprocess.call(cmd, shell = True)
            
            # delete og file
            fsu.delete_if_exists(abs_path)
            
            time.sleep(1)
             
            # rename temp file to og name
            fsu.rename_file_overwrite(temp_no_metadata_file_abs_path, abs_path)
            


# delete_all_metadata_from_all_mp4_in_dir(MOVIES_DIR_PATH)            
            
abs_path_l = fsu.get_dir_content_l(MOVIES_DIR_PATH, 'dir', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)

for abs_path in abs_path_l:
    print(abs_path)
    delete_all_metadata_from_all_mp4_in_dir(abs_path)
