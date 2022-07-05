# snoc's nightmare
## Problem Statement

...............my eyes

https://cyberclass-snocsnightmare.chals.io/

## Solution

View source.

In the HTML source, at the bottom of the file is the first part of the flag:

` <!-- part 1/3 of the flag: flag{cy4n_4nd_m -->`

Visiting the CSS file `style.css` linked in the head of the HTML document will give you the second part of the flag (scroll down to the bottom of the file):

`/* part 2/3 of your flag: ag3nt4_d0nt_l00k_ */`

Finally, visiting the JavaScript file `script.js` linked in the body will give you the last part of the flag:

`/* here's the last part of your flag: t00_b4d_t0g3th3r} */`

Combining all three parts:

`flag{cy4n_4nd_mag3nt4_d0nt_l00k_t00_b4d_t0g3th3r}`
