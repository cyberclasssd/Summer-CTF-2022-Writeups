ciphertext = '30 58 2d 57 2d 5a 7c 53 62 44 13 43 3d 41 7d 1 2e 3 31'
password = ''
key = "V4L0"
KEY_LENGTH=4
for i,c in enumerate(ciphertext.split()):
  password += chr( ord(key[i%KEY_LENGTH])^ int(c,16))

print(password)
