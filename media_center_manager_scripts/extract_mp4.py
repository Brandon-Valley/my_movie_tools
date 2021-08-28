from sms.file_system_utils import file_system_utils as fsu

def extract_mp4(search_dir, dest_dir):
    """
    Recurses into every nested dir in search_dir and puts all .mp4 files in dest_dir,
    priority given to last copied
    """
    
    
    file_l = fsu.get_dir_content_l(search_dir, 'file', 'abs_path', recurs_dirs = True)
    
    mp4_l = []
    for file in file_l:
        if fsu.get_extention(file) == '.mp4':
            mp4_l.append(file)
    
    
    fsu.copy_objects_to_dest(mp4_l, dest_dir)
    
if __name__ == "__main__":
#     search_dir = "D:\\test"
    search_dir = "D:\\Movies_and_TV\\Movies"
    dest_dir = "D:\\mp4_movies"
    extract_mp4(search_dir, dest_dir)
    print('done')