from who_is_on_my_wifi import *
from tqdm import tqdm
from time import sleep
def progress(range):
    for i in tqdm(range, desc ="Progress : "):
            sleep(.1)



WHO = who()
progress(WHO)
print("The Connected Devices Are : ")
for j in range(1, len(WHO)):
    print(f"The IP is {WHO[j][1]} And The Device name is {WHO[j][5]}")

input()
