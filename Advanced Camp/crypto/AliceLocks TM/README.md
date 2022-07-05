# AliceLocks&trade;
## Problem Statement

Alice is upgrading her AliceLocks&trade;! Or is it a downgrade . . .

Source code and ciphertext attached. Flag redacted in source.

## Solution
The `encrypt()` function encrypts each character one by one. Since `e` is small, the modulus will not have an effect, so just take the cube root of every character.

Flag: `flag{al1ce_l0cks_TM_m0re_like_al1ce_unL0cks_TM}`
