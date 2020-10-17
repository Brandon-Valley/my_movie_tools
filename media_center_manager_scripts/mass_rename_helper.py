
from sms.file_system_utils import file_system_utils as fsu

import os

def replace_in_filenames_in_dir(dir_path, find_str, replace_str):
    file_path_l = fsu.get_dir_content_l(dir_path, object_type = 'file', content_type = 'abs_path')
    
    for file_path in file_path_l:
        og_file_name = os.path.basename(file_path)
        
        replaced_file_name = og_file_name.replace(find_str, replace_str)
        
#         print('replaced_file_name: ', replaced_file_name, og_file_name)
        
        
        if og_file_name == replaced_file_name:
            print(find_str, 'not found in ', og_file_name, ' from ', dir_path)
        else:
            replaced_file_path = file_path.replace(og_file_name, replaced_file_name)
            print(replaced_file_path)
            
            fsu.rename_file_overwrite(file_path, replaced_file_path)





dir_path = 'C:\\vuze_downloads\\completed\\K-On!\\Season 2 - K-On!!'
find_str = '[HonokaSubs] K-ON! Season 2 - '
replace_str = 'K-ON! S02E'

replace_in_filenames_in_dir(dir_path, find_str, replace_str)