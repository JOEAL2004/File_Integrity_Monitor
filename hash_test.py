import hashlib

text='Hello Cybersecurity!'
data=text.encode('utf-8')

hash_object=hashlib.sha256(data)
hex_dig=hash_object.hexdigest()
print(f"SHA-256 hash of '{text}': {hex_dig}")