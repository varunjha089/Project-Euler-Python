"""
    Trying to create some directory at
    /
"""

import os

# path at which dir to be created
parent_dir = ''  # Pass the full dir path

for num in range(1, 300, 20):
    # Initial directory name
    directory = ""

    # a number is added at the last of each dir, incremented every time by 'for' loop
    directory += str(num) + "-" + str(num + 19)

    # joining directory to parent_dir
    path = os.path.join(parent_dir, directory)

    # creating the directory
    os.mkdir(path)

    # Printing the directory name
    print("directory '%s' created", directory)

print("Thanks for using the automation service")