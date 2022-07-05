# corrupted
## Problem Statement

We got sent this [image](./image.png), but it seems as if the file is broken. Can you find the flag?

## Solution

As the first hint suggests, we may not be dealing with an image file. To determine the true filetype, we can use the `file` command on the linux terminal. Run the command:

`file image.png`

We get this output:

`image.png: Zip archive data, at least v1.0 to extract, compression method=store`

So our image is actually a zip file. To make the computer treat it like a zip file, we need to change the file extension to `.zip`. This can be done with the following command:

`mv image.png image.zip`

Then, unzip this file, and enter the new directory we created:

`unzip image.zip`

`cd image`

Using `ls`, we find another image file: `1.png`. We can run `file` on this again to discover that we found another zip file. Change the file extension to zip, unzip the file, and enter the new directory. 

We keep doing this process for `2.png` until `5.png`. The second hint says that we can manually do this process and it will not take too long. Once we enter the `5` directory, we find our `flag.txt`! 

Flag: `flag{f1l3_3xt3ns10ns}`

