def print_flag():
    secret = open('flag.txt.enc', 'rb').read().decode()
    key = "potatoes"
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    decrypted = "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])
    print("Congrats, the password is correct! Here's your flag: " + decrypted)

user_input = input("Welcome! Please enter your password: ")
print("Sorry that is incorrect")
