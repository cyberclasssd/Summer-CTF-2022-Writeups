password = "REDACTED"
key = "REDACTED"
KEY_LENGTH=4

ciphertext = ""

for i,c in enumerate(password):
  ciphertext += hex(ord(c) ^ ord(key[i%KEY_LENGTH]))[2:] + " "

print(ciphertext)
