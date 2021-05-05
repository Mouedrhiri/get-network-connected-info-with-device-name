# Get Connected Devices Infos with Device Name By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

`from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

`from time import sleep`

### The I Used The Library Imaplib To Give Me Acces To Gmail Account

`import imaplib`

### I've Made a Function For The Progress Bar Like That :

    def progress(rang):
    for i in tqdm(rang, desc ="Progress : "):
            sleep(.1)

> As You All Can See I Made This Progress Bar Relative To The Searching Progress

---

# Let's Begin The Code Explanation :

> You Must Install WinPcap

## To Get All The Details About Connected Devices With Wifi By The Time I Used The Who Is On My Wifi Library

> `from who_is_on_my_wifi import *`

## The Library Give us a Lists Every list Contain IP Adress and Status

    ['IP Address:', '192.168.0.1', 'Mac Address:', 'FF:FF:FF:FF:FF:FF', 'Device:', 'Netcore Technology']

## What I Need From Here is Only The IP Adress and Device Name

> The Library Give Me The Result as a Matrix So I Will Iterate on Each Element in Each inside Specific Position and Print The Status

    for j in range(1, len(WHO)):
        print(f"The IP is {WHO[j][1]} And The Device name is {WHO[j][5]}")

---

Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)
