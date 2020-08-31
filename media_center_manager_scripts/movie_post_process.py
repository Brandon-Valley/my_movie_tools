

from sms.file_system_utils import file_system_utils as fsu
from sms.subprocess_utils import subprocess_utils as su

import os

PWD = os.path.dirname(os.path.abspath(__file__))

# test
movie_pwd = "D:\\test\\Chicken Run (2000) [720p]"


def delete_all_metadata_from_all_mp4_in_dir(in_dir_path):
    abs_path_l = fsu.get_dir_content_l(in_dir_path, 'file', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)
    
    for abs_path in abs_path_l:
        if fsu.get_extention(abs_path) == '.mp4':
            
            temp_no_metadata_file_abs_path = PWD + '//temp.mp4'           
            
            # delete temp file from previous test if exists
            fsu.delete_if_exists(temp_no_metadata_file_abs_path)
            
            # make temp file with deleted metadata
            cmd = 'ffmpeg -i "{}" -map_metadata "-1" -c:v copy -c:a copy "{}"'.format(abs_path, temp_no_metadata_file_abs_path)
            su.run_cmd_popen(cmd, print_output = False, print_cmd = True)#, shell = False, decode = False, strip = False, always_output_list = False, return_stderr = True)
            
            # delete og file
            fsu.delete_if_exists(abs_path)
             
            # rename temp file to og name
            fsu.rename_file_overwrite(temp_no_metadata_file_abs_path, abs_path)


if __name__ == '__main__':
    delete_all_metadata_from_all_mp4_in_dir(movie_pwd)
    print('done')