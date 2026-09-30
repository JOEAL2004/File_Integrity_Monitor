
import hashlib

def calculate_hash(filename):
  
  with open(filename,'rb') as file:
    data=file.read()

  hash_object=hashlib.sha256(data)
  hex_dig=hash_object.hexdigest()
  return hex_dig

if __name__ == "__main__":
  filename=input('Enter the filename to hash: ')
  result=calculate_hash(filename)
  print(f"SHA-256 hash of {filename}: {result}")
