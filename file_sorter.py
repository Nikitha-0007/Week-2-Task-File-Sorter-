import os
import shutil
from datetime import datetime

def sort_files_by_extension(directory):
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            ext = file.split('.')[-1]
            ext_folder = os.path.join(directory, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(os.path.join(directory, file), os.path.join(ext_folder, file))
    print("Files sorted by extension.")

def sort_files_by_date(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            folder_path = os.path.join(directory, date_folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))
    print("Files sorted by date.")

def sort_files_by_name(directory, keyword):
    name_folder = os.path.join(directory, keyword)
    os.makedirs(name_folder, exist_ok=True)
    for file in os.listdir(directory):
        if keyword in file:
            shutil.move(os.path.join(directory, file), os.path.join(name_folder, file))
    print(f"Files with '{keyword}' moved.")

if __name__ == "__main__":
    path = input("Enter the path to the directory: ").strip('"').strip("'")
    print("1. Sort by extension\n2. Sort by creation date\n3. Sort by name keyword")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        sort_files_by_extension(path)
    elif choice == '2':
        sort_files_by_date(path)
    elif choice == '3':
        keyword = input("Enter keyword to search in filenames: ")
        sort_files_by_name(path, keyword)
    else:
        print("Invalid choice.")
