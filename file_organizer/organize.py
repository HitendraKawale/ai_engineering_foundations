import os

path = "test_files"

list_of_files = os.listdir(path)

for i in list_of_files:
    name, ext = os.path.splitext(i)
    print(name, ext)
