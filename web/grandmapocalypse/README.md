# grandmapocalypse

## Problem Statement

The grandmas have now awoken, we believe that they are plotting something, please break into their bingo center and stop them quickly before it's too late!

[Source](./main.py)

## Solution

Browsing the source code, we see the route `/flag`, which gives us a flag if it passes an if statement.

```PYTHON
@app.route("/flag")
def flag():
    if "grandma" in request.cookies and check_cookie(request.cookies.get("grandma")):
        return send_file("./flag.txt")
    else:
        return "<h1>You are an IMPOSTER grandma!</h1>\n<h2>GET OUT OF OUR BINGO RESEARCH FACILITY CENTER NOW OR ELSE. </h2>"
```

Inside this if statement, we see that it must have a cookie named `grandma` and that the cookie must be valid, which is checked through a function call to `check_cookie`.

```PYTHON
def check_cookie(encrypted_cookie):
    decrypted_cookie = base64.b64decode(encrypted_cookie[::2]).decode("ascii")
    return decrypted_cookie == "1_4m_a_l337_6r4ndm4_wh0_l1k35_c00k135"
```

We see that `check_cookie` takes every other char of the cookie as a string (`encrypted_cookie[::2]`) and decodes it using base64 (`base64.b64decode`), then checks if the decoded string is equal to the expected string.

As such, we can base64 encode the decrypted_cookie string, getting `MV80bV9hX2wzMzdfNnI0bmRtNF93aDBfbDFrMzVfYzAwazEzNQ==` , which we can then pad with whatever characters we choose.

In the below case, we use curl, which is a command line utility for interacting with HTTP servers. We use the `/flag` endpoint, with the `--cookie` command line flag and we add the base64 decoded text padded with spaces.

```bash
curl http://website.site/flag --cookie "grandma=M V 8 0 b V 9 h X 2 w z M z d f N n I 0 b m R t N F 9 3 a D B f b D F r M z V f Y z A w a z E z N Q = ="
```

This gets us the flag.

`flag{w3_gr4ndm45_4r3_v3ry_displ34s3d_n0w}`
