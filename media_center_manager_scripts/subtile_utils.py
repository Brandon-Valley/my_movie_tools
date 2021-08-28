from sms.file_system_utils import file_system_utils as fsu
from sms.logger import txt_logger

SUBTITLE_AD_L = [
                    '-== [ www.OpenSubtitles.com ] ==-',
                    '== sync, corrected by elderman =='
                ]

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
    def group(seq, sep):
        g = []
        for el in seq:
            if el == sep:
                yield g
                g = []
            g.append(el)
        yield g
    
    og_lines = txt_logger.read(srt_file_path)
    print(og_lines)
    
#     timestamped_sub_ll = og_lines.split('')
    timestamped_sub_ll = list(group(og_lines, ''))
    
    print(timestamped_sub_ll)
    print(timestamped_sub_ll[-1])
    print(timestamped_sub_ll[-2])
    
    trimmed_timestamped_sub_ll = []
    for timestamped_sub_l in timestamped_sub_ll:
#         if any(subtitle_ad_line in SUBTITLE_AD_L for line in timestamped_sub_l):
        if any(item in SUBTITLE_AD_L for item in timestamped_sub_l):
            print('removed ad: ', timestamped_sub_l)
        else:
            trimmed_timestamped_sub_ll.append(timestamped_sub_l)
            
    print(trimmed_timestamped_sub_ll)
    print(trimmed_timestamped_sub_ll[-2])
    
    new_srt_lines = []
    for timestamped_sub_l in trimmed_timestamped_sub_ll:
        for srt_line in timestamped_sub_l:
            new_srt_lines.append(srt_line)
    print(new_srt_lines)
    
    txt_logger.write(new_srt_lines, srt_file_path)
    
    
#     new_srt_lines = []


if __name__ == "__main__":
#     dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test_dir\\Coming 2 America (2021) [Unknown]"
#     dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test_dir"
#     recursive = True
#     make_forced_copy_of_zzz_files_in_dir(dir_path, recursive)

    remove_ads_from_srt_file("C:\\Users\\Brandon\\Documents\\Other\\temp\\Game of Thrones - S04E01 - Two Swords (2011) [480p]\\Game of Thrones - S04E01 - Two Swords (2011) [480p].eng.srt")
    print('done')