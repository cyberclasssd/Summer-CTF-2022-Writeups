# Cypher
## Problem Statement

You start playing Valorant and are really interested in the Cypher agent. You hop into a match and try to defuse the bomb. In order to do so, you must determine the passcode of the explosive. Thankfully, you've managed to discover its source code (but the passcode and key are redacted), and the encrypted passcode. Find the password/flag.

Encrypted passcode: `30 58 2d 57 2d 5a 7c 53 62 44 13 43 3d 41 7d 1 2e 3 31`

## Hints

1. The *passcode* is in the format `flag{...}`. 
2. What do we know about the passcode that can allow us to extract information about the cipher itself?
3. How does this cipher apply a key of length 4 to encrypt plaintexts of any length? 
4. Remember that in python, `^` is XOR. Also remember that XOR is its own inverse: if `a XOR b = c`, then `c XOR b = a`.

## Solution

Note that the first 4 characters of the passcode/flag are `flag`. Also notice that the key length is 4, and upon examination of the source code, the key repeats. This is a form of a stream cipher, but very insecure since the keystream is repeating. It is also similar to a Vigenere cipher, but it uses XOR instead of a Ceasar shift.

We can consider the first 4 characters of the plaintext and ciphertext to determine what the key is. With the first 4 characters, `plaintext XOR key = ciphertext`, so `ciphertext XOR plaintext = key`, since XOR is self-inverting. Thus, we need to XOR the first 4 characters of the ciphertext with the first 4 characters of the plaintext (which are `flag`)

Also notice that the ciphertext is in hexadecimal byte form. That means each byte of the ciphertext correspond to 1 character of the plaintext.

We can convert the first 4 bytes of the ciphertext (`30 58 2d 57`) to binary, and convert the first 4 bytes of the plaintext (`flag`) to binary, giving us:

Ciphertext: `00110000 01011000 00101101 01010111`

Plaintext: `01100110 01101100 01100001 01100111`

XOR these together to get the key. In binary, we get `01010110 00110100 01001100 00110000`, or `V4L0` in ASCII. This is our key.

Now, we can use our key to decrypt the message. If we want to decrypt the ciphertext with Python, we need to convert the hexadecimal to decimal byte by byte, then XOR that value with the corresponding character of our key. Remember, our key length is 4 but it repeats, so the keystream is `V4L0V4L0V4L0...`. This has all been done in the solution script which is attached.

Solution: `flag{n0c4p_sku11x7}`
