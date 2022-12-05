from pathlib import Path
import os

import media_fsu

from sms.file_system_utils import file_system_utils as fsu

def put_stand_alone_media_files_in_dirs(in_dir_path):
    stand_alone_media_file_path_l = media_fsu.get_media_file_path_l(in_dir_path, recursive = False)
    
    for stand_alone_media_file_path in stand_alone_media_file_path_l:
        new_dir_path = os.path.splitext(stand_alone_media_file_path)[0]
        
        fsu.make_dir_if_not_exist(new_dir_path)
        
        og_file_name_with_ext = Path(stand_alone_media_file_path).name
        new_media_file_path = os.path.join(new_dir_path, og_file_name_with_ext)
        
        print("Copying {} to {}...".format(stand_alone_media_file_path, new_media_file_path))
        fsu.copy_object_to_path(stand_alone_media_file_path, new_media_file_path)
        
        print("  Deleting original stand-alone file: {}...".format(stand_alone_media_file_path))
        fsu.delete_if_exists(stand_alone_media_file_path)
    
    

if __name__ == "__main__":
    print('in main')

    in_dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test"
    put_stand_alone_media_files_in_dirs(in_dir_path)
    
    print('end of main')
    