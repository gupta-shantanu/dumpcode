import tkinter as tk
from urllib import request
from io import BytesIO
from PIL import Image,ImageTk
import base64
def getImage(url):
    '''
    root=tk.Tk()
    photo=getImage(url)
    lb=tk.Label(root,image=photo)
    '''
    
    img=request.urlopen(url)
    return ImageTk.PhotoImage(Image.open(BytesIO(img.read())))

    

if __name__=='__main__':
    print("enter web url of an image")
    url=input()
    root=tk.Tk()
    photo=getImage(url)
    lb=tk.Label(root,image=photo)
    lb.pack()
    root.mainloop()
