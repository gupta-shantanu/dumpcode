import requests
from bs4 import BeautifulSoup as bs
import tkimage


class Movie:
    def __init__(self,name="not found",rating=0.0,url=""):
        self.name=name
        self.rating=rating
        self.url=url
    def getPoster():
        return tkimage.getImage(self.url)
    def __str__(self):
        return self.name+" "+self.rating

        
def getMovie(movie):
    html=requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q="+movie+"&s=all")
    soup=bs(html.text,"html.parser")
    
    try:
        res=soup.table.tr.td.a['href']
    except:
        return Movie()

    html=requests.get("http://www.imdb.com"+res)
    soup=bs(html.text,"html.parser")
    
    name=soup.find("h1",{"itemprop":"name"})
    rating=soup.find("span",{"itemprop":"ratingValue"})
    
    image=soup.find("img",{"itemprop":"image"})
    try:
        url= image['src']
        return Movie(name.text,rating.text,url)
    except:
        return Movie()



if __name__=='__main__':
    while 1:
        movie=input()
        
        if movie=="exit":
            break
        response=getMovie(movie)
        print("Found movie:",response.name)
        print("Rating:",response.rating)

