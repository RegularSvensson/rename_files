
import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/eliasvensson/Udacity/full-stack/PFWP/rename_files/prank")
    os.chdir("/Users/eliasvensson/Udacity/full-stack/PFWP/rename_files/prank")
    saved_path = os.getcwd()
    
    #(2) for each file, rename filename
    for file_name in file_list:
    	print("Old Name - " + file_name)
    	print("New Name - " + file_name.translate(None, "0123456789"))
    	os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)


rename_files()
