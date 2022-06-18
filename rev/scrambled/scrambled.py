user_input = input("Please enter the password: ")
flag = ""
if len(user_input) != 25:
    print("The password is incorrect")
    exit()
index = 0
for i in range(len(user_input)):
    flag += user_input[len(user_input)-index-1]
    index += 3
    index = index % 25
if flag == "}i0d_10gfno_4nd{lgplngdma":
    print("The password is correct!")
else:
    print("The password is incorrect")
