import os
import shutil

path = "test_files"

list_of_files = os.listdir(path)

os.makedirs("results", exist_ok=True)

print(list_of_files)

for i in list_of_files:
    name, ext = os.path.splitext(i)

    ext_clean = ext[1:]

    os.makedirs(os.path.join("results", ext_clean), exist_ok=True)

    source = os.path.join(path, i)
    destination = os.path.join("results", ext_clean, i)
    shutil.move(source, destination)
