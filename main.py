import os
import shutil

def return_dir_info(path):

    if os.path.exists(path):
        subfolders = [os.path.split(i[0])[1] for i in os.walk(path)]
        arr = []

        for root, dirs, files in os.walk(path):
            arr += files

        return subfolders, subfolders + arr
    else:
        print('No such path!')

def remove_dir(path):

    areDirsInPath = False

    if os.path.exists(path):
        for i in os.walk(path):
            if i[0] != path and os.path.isdir(i[0]):
                areDirsInPath = True
                break

        if not areDirsInPath:
            shutil.rmtree(path)
        else:
            print('Can\'t delete directory, because there are subfolders inside')

    else:
        print('No such path!')

path1 = input('Type path: ')

a, b = return_dir_info(path1)
print(a)
print(b)

path2 = input('Type another path: ')

remove_dir(path2)