from PIL import ImageGrab
from win32 import win32api
import time as tk
import os
def screenshot():
    box = (470,209,700,211)
    im = ImageGrab.grab(box)
    im=im.convert('RGB')
    
##    im.save(os.getcwd() + '\\full_snap__  ' + str(int(time.time())) +
##'.png', 'PNG')
    return im
 
def check(im,k):
    for i in range(0,60+k):
        r,g,b =im.getpixel((i,0))
        r=r+g+b
        if r<400:
            if checkagain(im,i+50):
                tk.clock()
                return True
    return False
def checkagain(im,j):
    for i in range(j,30):
        r,g,b =im.getpixel((i,0))
        r=r+g+b
        if r<400:
            return False
    return True
k=0
while True:
    prev=k
    k=k+int(tk.clock()/100)
    if k>150:
        k=150
    if check(screenshot(),int(k)):
        win32api.keybd_event(0x20, 0,0,0)
   
    
