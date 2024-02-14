

from pathlib import Path
from sms.file_system_utils import file_system_utils as fsu
# from sms.subprocess_utils import subprocess_utils as su


import os
import argparse
import subprocess

PWD = os.path.dirname(os.path.abspath(__file__))

DEL_FILE_NAME_L = [
                    'folder.jpg',
                    'WWW.YIFY-TORRENTS.COM.jpg',
                    'www.YTS.MX.jpg',
                    'RARBG.txt',
                    'RARBG_DO_NOT_MIRROR.exe',
                    'www.YTS.AM.jpg',
                    'Torrent Downloaded From ExtraTorrent.cc.txt',
                    'ETRG.mp4',
                    'Torrent Downloaded From ProstyleX.com.txt',
                    'WWW.YTS.AG.jpg',
                    'Screenshots',
                    'ETRG.mp4'
#                     'movie.xml'
                  ]

# test
# movie_pwd = "D:\\test\\Chicken Run (2000) [720p]"


def delete_all_metadata_from_all_mp4_in_dir(in_dir_path):
    abs_path_l = fsu.get_dir_content_l(in_dir_path, 'file', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)
    
    for abs_path in abs_path_l:
        if fsu.get_extention(abs_path) == '.mp4':
            
            temp_no_metadata_file_abs_path = os.path.join(PWD, '//temp.mp4')
            
            # delete temp file from previous test if exists
            fsu.delete_if_exists(temp_no_metadata_file_abs_path)

            Path(temp_no_metadata_file_abs_path).parent.mkdir(parents=True, exist_ok=True)
            
            # make temp file with deleted metadata
            cmd = 'ffmpeg -i "{}" -map_metadata "-1" -c:v copy -c:a copy "{}"'.format(abs_path, temp_no_metadata_file_abs_path)
            print("Running {}...".format(cmd))
            with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1) as proc_obj:
                for line in proc_obj.stdout:
                    stripped_line = line.rstrip('\n')
                    print('[CMD] {}'.format(stripped_line))
            # su.run_cmd_popen(cmd, print_output = False, print_cmd = True)#, shell = False, decode = False, strip = False, always_output_list = False, return_stderr = True)
#             subprocess.call(cmd, shell = True)
            
            # delete og file
            fsu.delete_if_exists(abs_path)
             
            # rename temp file to og name
            fsu.rename_file_overwrite(temp_no_metadata_file_abs_path, abs_path)


def delete_extra_files(in_dir_path):
    abs_path_l = fsu.get_dir_content_l(in_dir_path, 'file', content_type = 'abs_path', recurs_dirs = False, rel_to_path = None)
    
    for abs_path in abs_path_l:
        if os.path.basename(abs_path) in DEL_FILE_NAME_L:
            fsu.delete_if_exists(abs_path)

    
    

if __name__ == '__main__':
                                                    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-m', '--movie_pwd', default = "D:\\test\\Chicken Run (2000) [720p]")
    args = parser.parse_args()

    
    delete_extra_files(args.movie_pwd)
#     delete_all_metadata_from_all_mp4_in_dir(args.movie_pwd)

#     add VVVVV !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     subtitle_utils -> remove_ads_from_all_nested_srt_files_in_dir
    
    
    
    
    
    print('done')