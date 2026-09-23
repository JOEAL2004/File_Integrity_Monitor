
import hashlib
filename=input('Enter the filename to hash: ')
with open(filename,'rb') as file:
  data=file.read()

hash_object=hashlib.sha256(data)
hex_dig=hash_object.hexdigest()
print(f"SHA-256 hash of {filename}: {hex_dig}")