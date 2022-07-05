# optiaw warp srahcek

## Problem Statement

https://cyberclass-optiaw-warp-srahcek.chals.io 

## Solution

First we can visit the site directly. This tells us to go to `/hello`.
```BASH
$ curl https://cyberclass-optiaw-warp-srahcek.chals.io/
/hello
```
So we curl to the /hello path, and get told to make a pita cookie with value wrap.
```BASH
$ curl https://cyberclass-optiaw-warp-srahcek.chals.io/hello
make a cookie called pita and set it to value wrap
```
So we can use the `-b` operator for curl. We are told to use user agent shrek
```
$ curl -b "pita=wrap" https://cyberclass-optiaw-warp-srahcek.chals.io/hello
set user agent header to shrek
```
We can do this with the `-A` flag. We find nothing in the response.
```
$ curl -b "pita=wrap" -A "shrek" https://cyberclass-optiaw-warp-srahcek.chals.io/hello

```
We can try adding the `-I` flag.
```
$ curl -b "pita=wrap" -A "shrek" -I https://cyberclass-optiaw-warp-srahcek.chals.io/hello
HTTP/1.1 200 OK
Set-Cookie: c00kie="flag{shr3k_n33ds_h3lp_3at1ng_p1t4}"; Path=/
Content-Length: 0
Connection: close
```
As such, we get the flag

```
flag{shr3k_n33ds_h3lp_3at1ng_p1t4}
```

