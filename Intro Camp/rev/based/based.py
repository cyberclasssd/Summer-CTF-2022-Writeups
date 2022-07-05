import base64
def check_password(password):
    encoded = base64.b64encode(password.encode('ascii'))
    return encoded == b'ZmxhZ3tCYXNlRF9Qcm9ncmFNbWVyfQ=='

user_input = input("Please enter the password: ")
if check_password(user_input):
    print("You are based!")
else:
    print("You are not very based")
