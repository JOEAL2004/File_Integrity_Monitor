import json
from pathlib import Path
from hash_test import calculate_hash


def save_baseline(file_hashes):
    with open("baseline.json","w") as file:
        json.dump(file_hashes, file, indent=4)

mode=input("Enter mode (create/monitor):").lower()
if mode not in ['create','monitor']:
    print("Invalid mode. Please enter 'create' or 'monitor'.")
    exit()
directory = input("Enter the directory to monitor: ")

file_hashes = {}

path = Path(directory)

if path.exists():
    print(f"The directory {directory} exists.")

    if path.is_dir():
        print("It is a directory.")

        for item in path.iterdir():

            if item.is_file():
                print(f"File: {item}")

                file_hash = calculate_hash(item)

                print(f"Hash: {file_hash}")
                file_hashes[item.name] = file_hash
        if mode=='create':
            save_baseline(file_hashes)
            print("Baseline created successfully.")
        elif mode=='monitor':
            try:
                with open("baseline.json", "r") as file:
                        baseline = json.load(file)
            except FileNotFoundError:
                print("Baseline file not found.Please create a baseline first.")
                exit()
            modified_count=0
            for item in file_hashes:

                if item in baseline:
                
                    if file_hashes[item] == baseline[item]:
                        print(f"File {item} is unchanged.")

                    else:
                        modified_count+=1
                        print(f"File {item} has been modified.")
                else:
                    print(f"File {item} is new.")

            print(f"Total modified files: {modified_count} times")
            for item in baseline:
                if item not in file_hashes:
                    print(f"File {item} has been deleted.")
            
    else:
      print("Error: The specified path is not a directory.")

else:
    print(f"The directory {directory} does not exist.")
