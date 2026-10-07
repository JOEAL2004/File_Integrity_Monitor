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
unchanged_count=0
modified_count=0
new_count=0
deleted_count=0
if path.exists():
    print(f"The directory {directory} exists.")

    if path.is_dir():
        print("It is a directory.")

        for item in path.iterdir():

            if item.is_file():
               

                file_hash = calculate_hash(item)
                file_hashes[item.name] = file_hash
        if mode=='create':
            save_baseline(file_hashes)
            print("Baseline created successfully.")
        elif mode=='monitor':
            try:
                with open("baseline.json", "r") as file:
                        baseline = json.load(file)
            except FileNotFoundError:
                print("Baseline file not found. Please create a baseline first.")
                exit()
            
            for item in file_hashes:

                if item in baseline:
                
                    if file_hashes[item] == baseline[item]:
                        print(f"File {item} is unchanged.")
                        unchanged_count+=1

                    else:
                        
                        print(f"File {item} has been modified.")
                        modified_count+=1
                       
                else:   
                    print(f"File {item} is new.")
                    new_count+=1

            
            for item in baseline:
                if item not in file_hashes:
                    print(f"File {item} has been deleted.")
                    deleted_count+=1
            print(f"Deleted files: {deleted_count}")
            
    else:
      print("Error: The specified path is not a directory.")
      exit()

else:
    print(f"The directory {directory} does not exist.")
    exit()

print("\n========== Security Summary ==========")
print(f"Unchanged files: {unchanged_count}")
print(f"Modified files:  {modified_count}")
print(f"New files:       {new_count}")
print(f"Deleted files:   {deleted_count}")

if modified_count == 0 and new_count == 0 and deleted_count == 0:
    print("Status: No integrity changes detected.")
else:
    print("Status: Integrity changes detected.")