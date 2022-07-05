def encrypt(msg, e, n):
  ret = []
  for char in msg:
    m = ord(char)
    ret.append(pow(m,e,n))
  return ' '.join(str(i) for i in ret)

print(encrypt("REDACTED", 3, 34081))
