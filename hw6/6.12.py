#!/usr/bin/env python

"""Matt O'Connell -- HW 6.12 Recursive Walk Dir"""

import os

def walk_dir(cd='.', root_name=None):
    if not root_name:
        root_name = cd
    root_name = os.path.split(os.path.abspath(root_name))[1]
    cd_path = os.path.abspath(cd)
    cd_accumulator = []
    cd_files = os.listdir(cd_path)

    # Loop through all cd files, add each by name
    for filename in cd_files:
        file_path = os.path.join(cd_path, filename)
        readable_name = root_name + file_path.split(root_name)[1]
        cd_accumulator.append(readable_name)
        # If file is a directory, recursively call walk_dir passing this file path as cd
        # Append the returned value to our accumulator
        if os.path.isdir(file_path):
            cd_accumulator = cd_accumulator + walk_dir(file_path, root_name)

    return filter(lambda file: '.DS_Store' not in file, cd_accumulator)


dirs = walk_dir('.')
d = '\n'.join(dirs)
print d
