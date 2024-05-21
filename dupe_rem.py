import os
import hashlib

def find_duplicates(directory) -> List:
    file_hashes = {}
    duplicate_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'rb') as file:
                hash_value = hashlib.md5(file.read()).hexdigest()
                if hash_value in file_hashes:
                    duplicate_files.append(file_path)
                else:
                    file_hashes[hash_value] = file_path

    return duplicate_files

def delete_duplicates(directory) -> None:
    duplicate_files = find_duplicates(directory)
    for file_path in duplicate_files:
        os.remove(file_path)
        print(f"{file_path} has been deleted.")

# Usage
def main() -> None:
    path = input("Path to folder or files: ")
    delete_duplicates(path)

if __name__ == "__main__":
    main()
