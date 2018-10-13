import os
import shutil
from random import randint

MAIN_PATH = '/home/kostyawh/files/'
EXTENSION = '.txt'

def sum_file(path):
    arr = []
    with open(path, 'rt') as fin:
        string = fin.readline()
        while string != '':
            arr.append(int(string))
            string = fin.readline()
    return sum(arr)

def create_files():
    for i in range(1,11):
        filename = MAIN_PATH + str(i) + EXTENSION
        with open(filename, 'wt') as fout:
            for j in range(3):
                fout.write(str(randint(1,100)) + '\n')

def sum_files():
    files = []
    sums = []

    for i in range(2):
        files.append(MAIN_PATH + str(randint(1,10)) + EXTENSION)

    print(files)

    for file in files:
        if os.path.exists(file):
          sums.append(sum_file(file))

    return sum(sums)


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

create_files()

print(sum_files())