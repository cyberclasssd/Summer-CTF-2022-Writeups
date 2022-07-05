n = 34081

#factor n using an online calculator
p = 197
q = 173

totient = (p - 1) * (q - 1)

d = 22475 #modular inverse of e mod totient. find using online calculator

def decrypt2(msg):
  return ''.join([chr(pow(i,d,n)) for i in [int(c) for c in msg.split()]])
