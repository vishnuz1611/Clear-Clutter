'''
Executables, Photos, Videos, Mp3, zip, pdf
'''

import os

import shutil

def scanner():
    source_dir = input("Path of directory to be organized: ")
    check = input("Do you want to remove empty directories (Y/N)?: ")
    # source_dir = r"C:\Users\whiskey\Downloads"
    items = {
        ".exe": "Executables",
        ".png": "Photos",
        ".jpg": "Photos",
        ".jpeg": "Photos",
        ".iso": "DiskImage",
        ".msi": "DiskImage",
        '.docx': "Documents",
        ".doc": "Documents",
        ".mp4": "Videos",
        ".mp3": "Audio",
        ".zip": "ZIP",
        ".pdf": "PDF"
    }
    isDir = os.path.isdir(source_dir)
    if not isDir:
        print('-----------------------')
        print("Enter a valid directory")
        print('-----------------------')
        scanner()

    for dirs in set(items.values()):
        path = os.path.join(source_dir, dirs)
        try:
            os.mkdir(path, 0o666)
        except:
            continue
    
    with os.scandir(source_dir) as files:
        for file in files:
            split = os.path.splitext(file.name)
            # print(split)
            source = os.path.join(source_dir, file.name)
            if split[1] in items:
                dest = os.path.join(source_dir, items[split[1]], file.name)
                shutil.move(source, dest)

            # Remove empty directories
            elif os.path.isdir(source) and check == 'Y':
                dir = os.listdir(source)
                if len(dir) == 0:
                    os.rmdir(source)
    
    print("Clutter Cleared !")


if __name__ == '__main__':
    scanner()

