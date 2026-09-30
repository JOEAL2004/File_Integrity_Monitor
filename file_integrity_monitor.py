from pathlib import Path
from hash_test import calculate_hash

directory=input('Enter the directory to monitor: ')

path=Path(directory)
if path.exists():
  print(f'The directory {directory} exists.')
  if path.is_dir():
    print('It is a directory.')
    for item in path.iterdir():
      if item.is_file():
        print(f'File:{item}')
  else:
    print('It is not a directory.')
else:
  print(f'The directory {directory} does not exist.')