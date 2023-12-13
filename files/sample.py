import shutil
import os
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content
def write_to_file(file_path, text_to_write):
    with open(file_path, 'r') as file:
        content = file.read()
    with open(file_path, 'w') as file:
        x = file.write(content+text_to_write)
def make_folder(folder_path):
    os.mkdir(folder_path)
def move_folder(file_path, new_file_path):
    shutil.move(file_path, new_file_path)
def make_file(file_path):
    open(file_path, 'w')
def rename_file(file_path, new_file_path):
    os.rename(file_path, new_file_path)
def delete_file(file_path):
    os.remove(file_path)
def list_files(file_path):
    return os.listdir(file_path)
def make_zip(origin_file, file_path):
    shutil.make_archive(origin_file, 'zip', file_path)
# x = read_file('C:/Users/conne/Videos/files/sample.txt')
# print(x)
# write_to_file('C:/Users/conne/Videos/files/sample.txt', 'ya like jazz????????????')
# make_folder('C:/Users/conne/Videos/files2')
# move_folder('C:/Users/conne/Videos/files/sample.txt', 'C:/Users/conne/Videos/files2')
# make_file('C:/Users/conne/Videos/files/file1.txt')
# make_file('C:/Users/conne/Videos/files/file2.txt')
# rename_file('C:/Users/conne/Videos/files/file1.txt', 'C:/Users/conne/Videos/files/renamed_file.txt')
# delete_file('C:/Users/conne/Videos/files/file2.txt')
# print(list_files('C:/Users/conne/Videos/files'))\
# make_zip('C:/Users/conne/Videos/files', 'C:\Users\conne\Downloads')