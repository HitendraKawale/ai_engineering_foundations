import os
import shutil

path = "test_files"

list_of_files = os.listdir(path)

os.makedirs("results", exist_ok=True)

print(list_of_files)

for filename in list_of_files:
    _, ext = os.path.splitext(filename)

    ext_clean = ext[1:]

    if not ext_clean:
        continue

    os.makedirs(os.path.join("results", ext_clean), exist_ok=True)

    source = os.path.join(path, filename)
    destination = os.path.join("results", ext_clean, filename)
    shutil.move(source, destination)
