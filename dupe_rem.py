import os
import hashlib

def find_duplicates(directory):
    file_hashes = {}
    duplicate_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'rb') as file:
                hash_value = hashlib.md5(file.read()).hexdigest()
                if hash_value in file_hashes:
                    duplicate_files.append(file_path)
                else:
                    file_hashes[hash_value] = file_path

    return duplicate_files

def delete_duplicates(directory):
    duplicate_files = find_duplicates(directory)
    for file_path in duplicate_files:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")

# Usage
delete_duplicates('./')
