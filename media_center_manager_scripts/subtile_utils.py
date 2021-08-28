from sms.file_system_utils import file_system_utils as fsu


# WRONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   
def make_forced_copy_of_zzz_files_in_dir(dir_path, recursive = False):
    file_path_l = fsu.get_dir_content_l(dir_path, object_type = 'file', content_type = 'abs_path', recurs_dirs = recursive, rel_to_path = None)
    
    for file_path in file_path_l:
        if file_path.endswith('.zzz.srt'):
            forced_file_path = file_path.replace('.zzz.srt', '.en.forced.srt')

            fsu.rename_file_overwrite(file_path, forced_file_path)
#             forced_file_path = file_path.replace('.zzz.srt', '.en.forced.srt')
#             print(forced_file_path)
#             
#             if not fsu.exists(forced_file_path):
#                 parent_dir_path = fsu.get_parent_dir_path_from_path(file_path)
#                 forced_file_name = fsu.get_basename_from_path(file_path, include_ext = True).replace('.zzz.srt', '.en.forced.srt')
#             
#                 print('creating {}...'.format(forced_file_path))
#                 
# #                 fsu.copy_objects_to_dest(file_path, forced_file_path)
#                 fsu.copy_object_to_dest_then_rename(file_path, parent_dir_path, forced_file_name)
#             else:
#                 print(forced_file_path, " already exists, not creating copy")


def remove_ads_from_srt_file(srt_file_path):
    og_lines = fsu


if __name__ == "__main__":
#     dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test_dir\\Coming 2 America (2021) [Unknown]"
    dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test_dir"
    recursive = True
    make_forced_copy_of_zzz_files_in_dir(dir_path, recursive)
    print('done')