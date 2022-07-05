# sqlnoir

## Problem Statement

I outlawed using `'` in the password, you won't be able to run an sql injection now >:)))).

Hint: The admin user is named `admin`.

## Solution

Although `'` is filtered in the password field, it's not filtered in the username field. Knowing that the admin user is named `admin`, we can run an sql injection with the payload 
username `admin'--`, and any password we choose. 

The serverside SQL injection now looks like this.

```SQL
SELECT id, username FROM `user` WHERE username='admin'--' AND password='anything'
```

As such, we get the flag

```
flag{h0w_r_u_so_c00l}
```
