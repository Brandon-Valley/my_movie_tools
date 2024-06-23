from pathlib import Path
import os
import shutil

def make_dir_if_not_exist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def copy_object_to_path(src_path_str, dest_path_str):
    shutil.copy(src_path_str, dest_path_str)

def delete_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def get_media_file_path_l(in_dir_path, recursive=False):
    media_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.m4v']
    media_files = []
    for root, dirs, files in os.walk(in_dir_path):
        for file in files:
            if any(file.endswith(ext) for ext in media_extensions):
                media_files.append(os.path.join(root, file))
        if not recursive:
            break
    return media_files

def put_stand_alone_media_files_in_dirs(in_dir_path):
    stand_alone_media_file_path_l = get_media_file_path_l(in_dir_path, recursive=False)
    
    for stand_alone_media_file_path in stand_alone_media_file_path_l:
        stand_alone_media_file_path = os.path.normpath(stand_alone_media_file_path)
        new_dir_path = os.path.splitext(stand_alone_media_file_path)[0]
        new_dir_path = os.path.normpath(new_dir_path)
        make_dir_if_not_exist(new_dir_path)
        
        og_file_name_with_ext = Path(stand_alone_media_file_path).name
        new_media_file_path = os.path.join(new_dir_path, og_file_name_with_ext)
        new_media_file_path = os.path.normpath(new_media_file_path)
        
        if Path(stand_alone_media_file_path).is_file():
            print(f"Copying {stand_alone_media_file_path} to {new_media_file_path}...")
            
            try:
                copy_object_to_path(stand_alone_media_file_path, new_media_file_path)
                print(f"  Deleting original stand-alone file: {stand_alone_media_file_path}...")
                delete_if_exists(stand_alone_media_file_path)
                print("    Success!")
            except FileNotFoundError as e:
                print(f"Error: {e}")
                delete_if_exists(new_dir_path)
                print(f"Failed to copy from {stand_alone_media_file_path} to {new_media_file_path}")
                raise Exception (
                    f"Failed to copy from {stand_alone_media_file_path} to {new_media_file_path}, this is probably "
                    "b/c the original file name is too long, please rename and retry")
        else:
            print(f"File does not exist: {stand_alone_media_file_path}")

if __name__ == "__main__":
    print('in main')

    in_dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test"
    put_stand_alone_media_files_in_dirs(in_dir_path)
    
    print('end of main')
