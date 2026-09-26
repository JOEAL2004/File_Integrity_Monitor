


from fileinput import filename
from pathlib import Path
dir=input('Enter the directory to parse: ')

path=Path(dir)
if path.exists():
    print(f"The directory {dir} exists.")
    for item in path.iterdir():
      if item.is_file():
        print(f"File: {item.name}")
      else:
        print(f"Directory: {item.name}")
else:
    print(f"The directory {dir} does not exist.")
      
