import os

print(os.listdir("E:/Datasets/glove.6B"))

path = "E:/Datasets/glove.6B/glove0d.txt"

print(os.path.exists(path))


file_path = "E:/hello_world.txt"
if os.path.exists(file_path):
    print("File already exists")
    file = open(file_path)
    print(file.read())
    file.close()
else:
    print("File did not exists")
    file = open(file_path, "w")
    file.write("Hello")
    file.close()
