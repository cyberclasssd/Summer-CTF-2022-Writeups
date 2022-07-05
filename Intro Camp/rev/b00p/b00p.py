def boop(noise):

  ret = ""
  
  for i in range(len(noise)):
    if (i % 2 == 0):
      ret += noise[i]
    else:
      ret += noise[len(noise) - i] 
  return ret == "f}ap{0lp00wf0gyl"

userInput = input("what noise are you making? ")

if (boop(userInput)):
  print("Good boop!")
else:
  print("bad boop..........")
