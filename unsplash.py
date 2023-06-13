from config import PEXELS_API_KEY
# install: pip install Pillow
from PIL import ImageFont , ImageOps
from PIL import Image
from PIL import ImageDraw
from pexels_api import API
import random
import requests
from config import UNSPLASH_API_KEY, UNSPLASH_SECRET_KEY
# def pexel_image():
#     #tags used tag1+ tag2
#     tag1 = ['space','moon','universe', 'stars', 'sky', 'autum', 'spring', 'winter', 'snow', 'mountain', 'jungle', 'ramadan', 'trees']
#     tag2 = ['sunrise','dawn','night', 'noon', 'sun', 'twilight', 'dawning', 'aurora', 'landscape','blurred', 'outdoors']
#     # tag3 = ['background','2040p','1080p','large','HD', 'wallpaper', ]
#     text = (random.choice(tag1)) + " " +(random.choice(tag2))  #+ " " + (random.choice(tag3)
#     # Create API object
#     # api = API(PEXELS_API_KEY)
#     # # Search five 'kitten' photos
#     # api.search(text, page=1, results_per_page=1)
#     # # Get photo entries
#     # photos = api.get_entries()
#     # # Loop the five photos
#     # for photo in photos:
#     #   # Print photographer
#     #   'Photographer: ', photo.photographer
#     #   # Print url
#     #   'Photo url: ', photo.url
#     #   # Print original size url
#     #   'Photo original size: ', photo.original
#     # response = requests.get(photo.original) # get photo

#     response = requests.get('https://api.unsplash.com/?client_id=7atV1M0J8Qa_d4gcNW09o5rfNkJodfWx2h-51u_Y1zQ')
#     # if response.status_code == 200: # check gateway response
#     #     with open(text+".jpg","wb") as file:
#     #         file.write(response.content)
#     # print('--------------Image Saved')
#     print (response.json())

# pexel_image()


import requests
import os

class Unsplash:
    def __init__(self,search_term,per_page=3,quality="full"):
        self.search_term = search_term
        self.per_page = per_page
        #self.page = 0
        self.quality = quality
        #self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5", "Host": "unsplash.com", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
        self.headers ={"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.5", "Connection": "keep-alive"}
    

    def set_url(self):
        #return f"https://unsplash.com/napi/search/photos?query={self.search_term}&xp=&per_page={self.per_page}&page={self.page}"
        #https://unsplash.com/napi/search?query={self.search_term}&xp=feedback-loop-v2:control&per_page={self.per_page}
        return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}"

    def make_request(self):
        url = self.set_url()
        return requests.request("GET",url,headers=self.headers)

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self,name):
        download_dir = "unsplash"
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,name)}.jpg"

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath,"wb") as f:
            f.write(requests.request("GET",url,headers=self.headers).content)

    def Scraper(self,pages):
        for page in range(0,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['photos']['results']:
                name = item['id']
                url = item['urls'][self.quality]
                # print(url)
                return str(url)
                # self.download(url,name)
                # return(url)
            self.pages += 1

if __name__ == "__main__":
    scraper = Unsplash("universe")
    y= scraper.Scraper(1)
    print(y)
    response = requests.get(str(y))
    # response = requests.get()
    if response.status_code == 200: # check gateway response
        with open("11.jpg","wb") as file:
            file.write(response.content)
    print('--------------Image Saved')
    print (response.json())
    


  