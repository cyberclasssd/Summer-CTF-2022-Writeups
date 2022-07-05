# grandma vault

## Problem Statement

I made a password vault, but I hashed my passwords. 
Only my friend john can find my password. The flag is the password wrapped in `flag{<password>}`.  So for example if the password is `password`, the flag will be `flag{password}`

## Solution

We can make a generic sql injection, which gives us our hash of `31435008693ce6976f45dedc5532e2c1`
Running this through john, we get a password of `thisismypassword`
```
john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```
As such, we get the flag

```

flag{thisismypassword}

```

