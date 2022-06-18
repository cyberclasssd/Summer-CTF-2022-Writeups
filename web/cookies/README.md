# cookies
## Problem Statement
do u kno da waye

https://unit-7-project-viviany2.csp-2-spring.repl.co/

## Solution
We start on this amazing webpage that is very epic and if you scroll to the bottom there’s a click me button!!! So you click it! which brings you to the “hidden page.”<br>

The first riddle asks you if theres an “html FORMS” page somewhere, prompting you to look for a `.html` file titled `forms`. Don’t use capitals.<br>

After going to `/forms.html` theres a form for you to fill out. You can fill in whatever you’d like into the two spaces it really doesn’t matter LOL.<br>

The form submission page presents another riddle (slay) which tells you the name of the page is a `.html` page with the name of a grocery store that has a similar name to that of a boy (starts with “ral”) and also has an s at the end. This is the grocery store Ralphs.<br>

After going to `/ralphs.html`, we are prompted to inspect the page, which gives us: 

```
So you did end up doing some INSPECTING! Congrats!!!!! Hm, now that I think about it, the man told me that his name was Mr. Hare
or something (??) and that he urgently needed to get to school...? Not sure who this "Mr. Hare" guy is, but maybe he likes
chocolate chip cookies... anyways, you should find him. I just searched him up, and he can be found at a place called "CCA."
(hint...don't use capitals when typing in the url :D)
```

Since we know this "Mr. Hare" guy can be found at CCA (no capitals -> cca), we can guess that the next page is `/cca.html`.<br>

The page `/cca.html` tells us that the next page is Mr. Hare's classroom, and that the classroom starts with an F, there are three digits following the F, and that they add up to a 7. The room numbering system at cca (if you were not aware) is a letter followed by three numbers, and since the classroom is on the first floor, we know the first number must be 1. The second number is zero because CCA doesn't have more than 10 classrooms per building per floor, and thus the third number must be 6 (or you could guess and check with the second and third number adding up to 6 but that takes a while). So our next page is `/f106.html`.<br>

The page `/f106.html` literally tells us to go to "ALLTHECOOKIES" with no capitals and an `.html` at the end, so thats what we do!<br>

This page tells us we must find the "Hare Lair," and the hint is that there might be hyphens. Hyphens typically separate spaces between words, and since we know theres a `.html` at the end, the page we are looking for must be `/hare-lair.html`!<br>

The hare lair tells us to hover over things... we can see some of the text boxes tell us we are "close," or that the answer is "not here!" but if we scroll to the bottom and hover over the website, it tells us: 
```
:O u made it! try "/riddle.html" ?
```
So our next page is `/riddle.html!`<br>

`riddle.html` gives us a riddle (as the name suggests). The riddle:
```
I’m usually made of sugar, chocolate is a delight! I crumble into bits, won’t you please take a byte?
```
The whole theme of this web chall is cookies, and "cookie" is also the answer to the riddle!(if you googled you would have found a reddit page with the same answer #slay but no googling is allowed!) Thus our next page is `/cookiehello.html`, as we are told by the hint.<br>

The page `/cookiehello.html` tells us to inspect! And when we inspect and scrooooooool down a lot, we see this: 
```
wow! you found the hidden message :D just like the first hidden website, not many people get to this point! congratulations!
here's a gift i got for you: "aHR0cHM6Ly9mb3Jtcy5nbGUvRHVDa1I1NnhoQURKaFp1VTY=". what is this weird string of text? hm, maybe
its been encoded with a certain base??
```
This looks like base64, so let's use an online decoder and decode the "gift" we were given. Decoding the text in quotes gives: https://forms.gle/DuCkR56xhADJhZuU6, so let's go to the form!<br>

Fill out the form!! Make sure you select that you LIKE chocolate chip cookies ;) or else you might not be able to continue!! Once we've filled out the form we're told to head to `/aslkjdpwoeinvlaksjpe.html` to keep playing!<br>

The page of `/aslkjdpwoeinvlaksjpe.html` tells us to fill out another form :) so we do! And this brings us to the form response page, where we see a final message with a cookie reward >:OOOOOOO finally!!! But most of us were looking for a flag, weren't we? The message tells us to look at the capital letters, which, if you look closely, spell out the word `INSPECT`. So we inspect the page, bringing us to the FINAL FLAG (FINALLY!!!!!!!!!)

Final Flag: `flag{y0u_g0t_411_th3_c00k1es_y4y_1203984}`
