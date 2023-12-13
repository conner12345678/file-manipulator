
# File Manipulator

The objective of this was to make a python program that could manipulate files by doing stuff such as creating files, renameing files and moving files.

read_file(): This function does exactly what it says, it reads the file in the python terminal. It uses a with function to set the file path equal to a file, after that it uses a file.read function to input the contents of the file into the terminal.

write_to_file(): This fi=unction writes new content in the file without geting rid of the old content that the file contains. It does this by setting a variable equal to the contents of the file path, which is the same function that is used to read the file in read_file(). After setting a variable equal to the file.read you can add the contents that you want to add to the end of the old contents without the risk of getting rid of all of the other text in the file.

make_folder(): This does exactly what it says, it makes a folder. When you give the function a file path it uses the os.mkdir(file_path) to create a new folder in the file ppath that you gave it.

make_file(): Similar to the make_file() function this function makes a file in a specified file path. This uses the open(file_path, 'w') to open a new file in the file path that is for writing.

move_folder(): This moves the folder from one file path to another file path. This uses the shutil.move program to move the folder from one area to another using file_path and new_file_path

rename_file(): This function renames a file from what it was to somthing new. Rename_file() uses os.rename(file_path, new_file_path) to remake a specific file in a file path with a new name.

delete_file(): This function deletes a file from a specified file path. This uses os.remove(file_path) to remove the specific file path so if you used os.remove(C:users/you/videos/folder/video.png) it would remove the video.png from the folder in videos

list_files(): This lists the specific files in a specific folder for you. This uses os.listdir(file_path) to list the specific files inside of the file path that was given to the function
## Authors

- [@conner12345678](https://github.com/conner12345678/3DGameGit)

