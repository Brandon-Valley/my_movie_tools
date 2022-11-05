from sms.file_system_utils import file_system_utils as fsu
from sms.logger import txt_logger
from pathlib import Path
import subprocess

import media_fsu

SUBTITLE_AD_L = [
                    '-== [ www.OpenSubtitles.com ] ==-',
                    '== sync, corrected by elderman ==',
                    'Sync & corrections by honeybunny',
                    'www.addic7ed.com'
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
#     print(og_lines)
    
#     timestamped_sub_ll = og_lines.split('')
    timestamped_sub_ll = list(group(og_lines, ''))
    
#     print(timestamped_sub_ll)
#     print(timestamped_sub_ll[-1])
#     print(timestamped_sub_ll[-2])
    
    trimmed_timestamped_sub_ll = []
    for timestamped_sub_l in timestamped_sub_ll:
#         if any(subtitle_ad_line in SUBTITLE_AD_L for line in timestamped_sub_l):
        if any(item in SUBTITLE_AD_L for item in timestamped_sub_l):
            print('removed ad: ', timestamped_sub_l, srt_file_path)
        else:
            trimmed_timestamped_sub_ll.append(timestamped_sub_l)
            
#     print(trimmed_timestamped_sub_ll)
#     print(trimmed_timestamped_sub_ll[-2])
    
    new_srt_lines = []
    for timestamped_sub_l in trimmed_timestamped_sub_ll:
        for srt_line in timestamped_sub_l:
            new_srt_lines.append(srt_line)
#     print(new_srt_lines)
    
    txt_logger.write(new_srt_lines, srt_file_path)
    
    
def remove_ads_from_all_nested_srt_files_in_dir(dir_path):
    file_path_l = fsu.get_dir_content_l(dir_path, object_type = 'file', content_type = 'abs_path', recurs_dirs = True)
    
    for file_path in file_path_l:
#         print(file_path)
#         print(fsu.get_basename_from_path(file_path))
        if fsu.get_basename_from_path(file_path).endswith('.srt'):
#             print(file_path)
            remove_ads_from_srt_file(file_path)
             
          
# Added OpenSubtitles creds with: filebot -script fn:configure
def download_subtitles_for_single_media(media_file_path):
#     cmd = 'filebot -script fn:suball "{}"'.format(media_file_path) 
#     cmd = 'filebot -script dev:osdb.explain "{}" [-non-strict] --def fetch=y'.format(media_file_path) 

    # only seems to download .eng.srt
    cmd = 'filebot -get-subtitles -r "{}" -non-strict'.format(media_file_path) 
    subprocess.call(cmd, shell = False)
    
    
def download_subtitles_for_all_media_files_in_nested_dirs(in_dir_path):
    '''Downloads subtitle file(s) next to each media file, so all media files should be in their own dir before running this'''
    media_file_path_l = media_fsu.get_media_file_path_l(in_dir_path = in_dir_path, recursive = True)
    
    for media_file_path in media_file_path_l:
        print("Downloading subtitles for {}...".format(media_file_path))
        download_subtitles_for_single_media(media_file_path)


if __name__ == "__main__":
    print('in main')
#     dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test_dir\\Coming 2 America (2021) [Unknown]"
#     dir_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\test_dir"
#     recursive = True
#     make_forced_copy_of_zzz_files_in_dir(dir_path, recursive)

#     remove_ads_from_srt_file("C:\\Users\\Brandon\\Documents\\Other\\temp\\Game of Thrones - S04E01 - Two Swords (2011) [480p]\\Game of Thrones - S04E01 - Two Swords (2011) [480p].eng.srt")
#     remove_ads_from_all_nested_srt_files_in_dir("C:\\Users\\Brandon\\Documents\\Other\\temp\\Game of Thrones - Season 4 (2011)")
#     remove_ads_from_all_nested_srt_files_in_dir("D:\\Movies_and_TV\\TV\\Game of Thrones\\Game of Thrones - Season 4 (2011)")
    
    
    
    test_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\Baby Driver (2017) [1080p]\\Baby Driver (2017) [1080p].mp4"
    test_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\Baby Driver (2017) [1080p]"
#     test_path = "C:\\Users\\Brandon\\Documents\\Other\\temp"
#     test_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\A Quiet Place Part II (2021)\\A Quiet Place Part II (2020).mp4"
#     test_path = '"A Quiet Place Part II (2020)"'
#     download_subtitles_for_single_media(test_path)
    download_subtitles_for_all_media_files_in_nested_dirs(test_path)
    
    print('end of main')
    
    
    
    
    
    print('done')