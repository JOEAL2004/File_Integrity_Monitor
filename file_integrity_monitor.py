import json
from pathlib import Path
from hash_test import calculate_hash

directory=input('Enter the directory to monitor: ')
file_hashes={}
path=Path(directory)
if path.exists():
  print(f'The directory {directory} exists.')
  if path.is_dir():
    print('It is a directory.')
    for item in path.iterdir():
      if item.is_file():
        print(f'File:{item}')
        file_hash=calculate_hash(item)
        print(f'Hash: {file_hash}')
        file_hashes[item.name]=file_hash
    
    json.dump(file_hashes,open('baseline.json','w'))
    baseline=json.load(open('baseline.json','r'))
    print(baseline)
  else:
    print('It is not a directory.')
else:
  print(f'The directory {directory} does not exist.')