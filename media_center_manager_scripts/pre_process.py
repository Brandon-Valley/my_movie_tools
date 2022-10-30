# meant to be run before media center master
# all processing on movies should be done in the vuze completed dir

# import os
# 
# SCRIPT_PARENT_DIR = os.path.abspath(__file__)
# 
# os.chdir(SCRIPT_PARENT_DIR)
import subtile_utils


if __name__ == '__main__':
    try:
        ## your code, typically one function call
        import os, sys
        sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) # to import from parent dir
        
        import delete_metadata_from_mp4_files_in_nested_dirs
         
        # COMPLETED_DIR_PATH = 'C:\\vuze_downloads\\completed' 
        COMPLETED_DIR_PATH = "D:\\working"
         
         
        print('Running Pre-Process on: ', COMPLETED_DIR_PATH)
         
        print('Deleting metadata from .mp4 files...')
        delete_metadata_from_mp4_files_in_nested_dirs.delete_all_metadata_from_all_mp4_in_movie_dirs(COMPLETED_DIR_PATH)
        
        
        input('Pre-Process Complete, Now Run Media Center Master, Press enter to close.')
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
        print("Press Enter to continue ...")
        input() 

