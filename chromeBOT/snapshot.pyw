from PIL import ImageGrab
from win32 import win32api
import os
import time

def screenGrab():
    box = (390,210,580,212)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()


win32api.keybd_event(0x20, 0,0,0)
