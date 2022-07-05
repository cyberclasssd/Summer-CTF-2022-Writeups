def encrypt(msg, e, n):
  ret = []
  for char in msg:
    m = ord(char)
    ret.append(pow(m,e,n))
  return ' '.join(str(i) for i in ret)

print(encrypt("REDACTED", 3, 74359630962348618997013019039837388856339849662252499901639869849780497981603))
