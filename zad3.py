from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

with open("example.txt", "rb") as f:
    message = f.read()

h = SHA256.new(message)
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(h)

with open("signature.sig", "wb") as f:
    f.write(signature)
