Welcome to the flag checker! Here, you can submit the flag to check if it is correct. You might see a few numbers in the code, but I'm not sure what it represents yet.
<br>
Download here: <a href="numbers.py">numbers.py</a>
## Solution
The input array is populated with the user input, where the element represents which index of string `a` it is. This means that if it was `0`, the character would be `a`, if the number was `25`, the character would be `z`, etc. Therefore, we just need to check what is inside the check array and turn it into characters. `5` points to `f`, `11` points to `l`, `0` points to `a`, `6` points to `g`, and so on. 

| 5 | 11 | 0 | 6 | 76 | 28 | 14 | 13 | 47 | 4 | 17 | 19 | 62 | 2 | 40 | 39 | 21 | 30 | 17 | 45 | 62 | 2 | 14 | 13 | 21 | 4 | 43 | 45 | 77 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f | l | a | g | { | C | o | n | V | e | r | t | _ | c | O | N | v | E | r | T | _ | c | o | n | v | e | R | T | } |


Our flag is then `flag{ConVert_cONvErT_conveRT}`
