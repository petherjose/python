import os

def rename_files():
    file_list = os.listdir(r"./prank")
    #print(file_list)
    saved_path = os.getcwd()

    absolute_path = saved_path + r"/prank/"
    print(absolute_path)
    os.chdir(absolute_path)
        
    for file_name in file_list:
        newName = file_name.translate(None, "0123456789")
        os.rename(file_name, newName)
        print("Old name: " + file_name)
        print("New name: " + newName)


rename_files()
