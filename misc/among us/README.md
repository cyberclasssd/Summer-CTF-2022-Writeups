# among us
## Problem Statement

Find the impostor in this [zip file](./amogus.zip).

## Solution

Unzip the zip file. Inside, you will find many directories, numbered 1-1000. In each of these directories, there is a text file named `<directory number>.txt`. These files contain a fake flag. However, there is one text file that is named `flag.txt`, which contains the true flag. 

You can manually search each directory for the flag. However, this will take a long time. There is a faster way through the Linux terminal. using the `find` command, we can list out every file in this directory and sub-directories. We can use `grep` to search for the file we want, `flag.txt`. After we unzip the file and enter the directory, we can use the following command to find where our `flag.txt` file is.

`find * | grep flag`

This searches for all files in the directory and sub-directories, and outputs files that contain `flag` in their name. The output of the command is:

`405/flag.txt`

Now, we know that our flag is in the `405` directory. Open this directory, and read the text file. We will get the flag!

Flag: `flag{imp0st0r_sus}`

