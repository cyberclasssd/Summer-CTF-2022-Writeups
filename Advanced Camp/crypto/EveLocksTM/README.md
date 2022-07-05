# EveLocksTM
## Problem Statement
Who would've thought that we shouldn't trust Eve to make locks . . .
## Solution
The public exponent is small, but simply finding the cube root of c does not work. However, because we know that m^3 = kn + c based off of the modular exponentiation equation, we can guess non-zero values of k to find a value of kn + c that is a cube number. Sure enough, the cube root of n + c (k = 1) will be equal to m.

Flag: `flag{eEee3eee_3eeE3e3_EEe3EEeeeee}`
