# sharknet
## Problem Statement
connect to the ultra-secure sharknet! definitely secure.

## Solution
Open the file in Wireshark and follow the TCP stream. Since the network traffic uses the TELNET protocol, the traffic is not encrypted, and the username and password are transmitted in plaintext.

![image](https://user-images.githubusercontent.com/69173442/174423545-dd56aa5d-4c2b-40e5-ac71-f573f9653a74.png)


The flag is the TELNET password: `flag{TELNET_d03snt_eNcrypt_tr4ff1c}`
