import zipfile
import os

main_Path = './'
files = []

for files in os.listdir(main_Path):
    if files.endswith((".zip")):
        full_Path = main_Path + "\\" + files
        compressedFile_zip=zipfile.ZipFile(full_Path)
        compressedFile_zip.extractall(main_Path)
        compressedFile_zip.close()
        os.remove(full_Path)
