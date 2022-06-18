Someone wrote a password checker but forgot to finish coding it. Please help him and solve this challenge! <br>
Click here to download the two files: <a href="fixed.py" download>based.py</a> <a href="flag.txt.enc" download>flag.txt.enc</a> <br>
(You need to run the python program with flag.txt.enc in the same directory for it to work)
<br><br>
## Solution:
After looking at the code for a bit, we notice that the print_flag() function is what prints the final flag. However, it is never run, so all we need to do is just somehow run the code. Since we can freely add any code we want into the file, we just add print_flag() to the bottom of the code and we get our flag outputted, which is: `flag{Add1ng_c0de}`
