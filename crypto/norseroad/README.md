# norse road
## Problem Statement
Looking around on an old norse road  
Traveling on a tall horse, rode  
Down the long path, reading this coarse ode  
Wondering where to find the source code.

Hint: the flag is all lowercase and in standard flag format

> ABCCCCBCCBCCCB/BCCBCCCB/BACBAAABAB/BCABACACBABCCABCABCACCBCACCBACAAB/BACCCBCCBACBCABCACBACAAB/BCABACBACCB/BABCCCCBCB/BCCACBCACCBCABAACB/BCCBCCCB/BACACBCAAAABCACBACACBCCABAACCCBCCCCABCACBCAACBCACBCAAAABCCCBAA

## Solution
This is simply morse code. Looking at the long string, we can safely assume that B represents spaces based on its frequency and how it surrounds every "/".
Then, we are left to figure out what A and C represent. After trial and error, the correct replacements are when "C = "." and "A" = "-". The resulting morse code string is
> \- .... .. ... / .. ... / -. --- - / .- -.-. - ..- .- .-.. .-.. -.-- / -... .. -. .- .-. -.-- / .- -. -.. / - .... . / ..-. .-.. .- --. / .. ... / -.-. .---- .-. -.-. ..- --... ....- .-. .--. .-. .---- ... --

Which decodes to
>THIS IS NOT ACTUALLY BINARY AND THE FLAG IS C1RCU74RPR1SM

`flag{c1rcu74rpr1sm}`
