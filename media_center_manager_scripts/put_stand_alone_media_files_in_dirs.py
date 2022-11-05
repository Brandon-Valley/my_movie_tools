import media_fsu

def put_stand_alone_media_files_in_dirs(in_dir_path):
    stand_alone_media_file_l = media_fsu.get_media_file_path_l(in_dir_path, recursive = False)
    print(stand_alone_media_file_l)
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    print('in main')

    in_dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test"
    put_stand_alone_media_files_in_dirs(in_dir_path)
    
    print('end of main')
    