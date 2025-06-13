from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as f:
        data = f.read()
    data = pad(data)
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(data)
    
    with open(file_name + ".enc", 'wb') as f:
        f.write(cipher.iv + encrypted)

key = get_random_bytes(16) 
with open("secret.key", "wb") as f:
    f.write(key)

encrypt_file("example.txt", key)
