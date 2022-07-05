I have the flag, but it is scrambled! Can you try and help me unscramble the flag? <br>
Link: <a href = "scrambled.py" download>scrambled.py</a>
<br><br>
## Solution
Flag is originally blank, and we populate flag inside the for loop. This means the main part of the code that we need to check is the for loop. We notice that there's another variable called index and it originally gets set equal to 0. It then adds three every time the loop runs once. We then mod index by 25. This is essentially the same thing as if index is bigger than or equal to 25, we subtract it by 25. <br>
If we take a look at the line `flag += user_input[len(user_input)-index-1]`, we notice that we add a character from our user input into our string flag, and the index of this character is determined by `len(user_input)-index-1`, which is essentially `24-index` since the length of user_input HAS to equal to 25 (we checked if the length of user_input is not 25 we will exit the code). If we write down what `24-index` is for every time the loop runs, we eventually end up with the following indices: 
```
24, 21, 18, 15, 12, 9, 6, 3, 0, 22, 19, 16, 13, 10, 7, 4, 1, 23, 20, 17, 14, 11, 8, 5, 2
```
These numbers mean that the first character of flag is equal to the 25th character (since python is 0-indexed) of our input, character 2 of flag is equal to the 22nd character of our input, character 3 of flag is equal to the 19th character of our input, and so on. Since we know what flag is (the line `flag == "}i0d_10gfno_4nd{lgplngdma"` essentially means that we want flag to equal to that string in order for the result to be true), we just need to work backwards to find what our input should be in order for flag to be that. Using what we found out earlier, we map each character of flag to the character of our input and we get our final flag of: 
`flag{m0dd1ng_4nd_l0oping}`
