def get_non_nested_media_file_path_l(in_dir_path): 
    ''' Returns list of abs path strings to every .mp4, .mkv, and .avi file under in_dir_path recursively'''
    pattern_l = ('*.mp4', '*.mkv', "*.avi") # the tuple of file types
    
    media_file_path_l = []
        
    for pattern in pattern_l:
        pattern_media_file_path_str_l = list(path_obj.__str__() for path_obj in Path(in_dir_path).rglob(pattern))
        media_file_path_l.extend(pattern_media_file_path_str_l)

    return(media_file_path_l) 