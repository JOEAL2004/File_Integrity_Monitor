import json
from pathlib import Path
from hash_test import calculate_hash

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

        # Load the existing baseline
        with open("baseline.json", "r") as file:
            baseline = json.load(file)

        # Compare current hashes with baseline
        for item in file_hashes:

            if item in baseline:
               
                if file_hashes[item] == baseline[item]:
                    print(f"File {item} is unchanged.")

                else:
                    print(f"File {item} has been modified.")

            else:
                print(f"File {item} is new.")
          
        for item in baseline:

          if item not in file_hashes:
              print(f"File {item} has been deleted.")
    else:
      print("It is not a directory.")

else:
    print(f"The directory {directory} does not exist.")