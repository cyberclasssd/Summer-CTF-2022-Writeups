a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_!@#$%^&*()-+={}"
user_input = input("Welcome to the flag checker. Enter a flag to check if it's correct: ")
if len(user_input) != 29:
    print("Sorry, that flag is incorrect")
    exit()
input = []
check = [5, 11, 0, 6, 76, 28, 14, 13, 47, 4, 17, 19, 62, 2, 40, 39, 21, 30, 17, 45, 62, 2, 14, 13, 21, 4, 43, 45, 77]
for i in user_input:
    input.append(a.index(i))
for i in range(len(input)):
    if input[i] != check[i]:
        print("Sorry, that flag is incorrect")
        exit()
print("The flag is correct!")
