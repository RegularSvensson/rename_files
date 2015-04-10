
import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/eliasvensson/Udacity/full-stack/PFWP/rename_files/prank")
    os.chdir("/Users/eliasvensson/Udacity/full-stack/PFWP/rename_files/prank")
    saved_path = os.getcwd()
    
