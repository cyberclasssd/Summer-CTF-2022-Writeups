# Metaverse NFTs
## Problem Statement

I just screenshotted your [NFT](./NFT.png)! You are going to lose all your DonkeyCoins in the Metaverse!!!

## Solution

View the exif metadata of this image to find some information. The following is output of the `exiftool` command on a Linux terminal, but you can get the same output from an online exif metadata viewer like the one [here](https://exifdata.com/) (you will need to click the `Detailed` button). 

```
ExifTool Version Number         : 12.41
File Name                       : NFT.png
Directory                       : .
File Size                       : 198 KiB
File Modification Date/Time     : 2022:06:16 19:17:58-04:00
File Access Date/Time           : 2022:06:16 19:17:58-04:00
File Inode Change Date/Time     : 2022:06:16 19:17:58-04:00
File Permissions                : -rwxrw-rw-
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
XMP Toolkit                     : Image::ExifTool 12.41
Creator                         : flag{Inv3stIn
Copyright Notice                : D0nk3yC0in}
Application Record Version      : 4
Image Size                      : 600x600
Megapixels                      : 0.360
```
We can notice that there are 2 entries here that look like parts of a flag: `flag{Inv3stIn` and `D0nk3yC0in}`. Combining these together, we can get our flag!

Flag: `flag{Inv3stInD0nk3yC0in}`

