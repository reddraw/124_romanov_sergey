import os
directory=str(input("Введите путь в директорию"))
def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            print("Файл-" + filename)
        for directories in dirs:
            print("Папка-" + directories)
print(print_docs(directory))