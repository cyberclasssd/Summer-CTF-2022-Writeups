# iiceiice baby i love shaved ice
## Problem Statement

Shaved ice is so epic! This is a png image of my FAVORITE shaved ice ever... OH WAIT its gone?!!?!1 There is some trouble aHEAD for those who have stolen my beloved shaved ice.

Fix the image. Find the flag. Bring me back my beloved shaved ice.

Hint: remember... what type of image is this?

## Solution
The problem statement hints to us that the image needs to be "fixed." There is also a hint to "header" in the word "aHEAD." 

![image](https://user-images.githubusercontent.com/100059668/176829443-44fff674-ed5c-4673-ae53-cb8092d6bc08.png)

Inputting the broken PNG image into https://hexed.it/ shows us that the first 8 bytes, or the file signature, is ``38 E0 FF B2 99 0A 2A 3D`` instead of ``89 50 4E 47 0D 0A 1A 0A`` as they should be.

<img width="1045" alt="image" src="https://user-images.githubusercontent.com/100059668/176829646-5e9082ec-d4da-411e-8bff-4687386cafcb.png">

Exporting the new bytes gives us an image of our shaved ice! And a flag :)

![iceeeeee](https://user-images.githubusercontent.com/100059668/176829731-10aac44f-ca4c-471d-b28d-9ff0a665daa8.png)

## Flag: ``flag{yuMmY_sh4v3d_1c3_y4y_s0_3p1c}``. 

Thank you for saving my beloved :')
