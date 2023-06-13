# install: pip install --upgrade arabic-reshaper
from arabic_reshaper import ArabicReshaper
configuration = {
    'delete_harakat': False,
    'support_ligatures': False,
    'delete_tatweel' : False,
    'shift_harakat_position' : False,
    'use_unshaped_instead_of_isolated' : True
}
# install: pip install python-bidi
from bidi.algorithm import get_display
from config import PEXELS_API_KEY
# install: pip install Pillow
from PIL import ImageFont , ImageOps
from PIL import Image
from PIL import ImageDraw
from pexels_api import API
import requests
# Type your Pexels API
# create search term random
import random

from bs4 import BeautifulSoup
from serialcode import *

def create_image(imageFile, texts):
    # this was a 400x400 jpg file
    imageFile = imageFile+".jpg"

    # load the font and image
    font = ImageFont.truetype("Al Majeed Quranic Font Regular", 45)
    image = Image.open(imageFile)
    image =image.resize((1080,1080))
    # image.save('1.jpg')

    # first you must prepare your text (you dont need this step for english text)
    sura, text =  [texts.contents[1].contents[0], texts.contents[0]]

    #text length adjustment

    #arabic reshaper
    reshaper = ArabicReshaper(configuration=configuration)
    reshaped_text = reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)    # correct its direction

    # start drawing on image
    draw = ImageDraw.Draw(image)
    #text dimensions
    txtlength,txtheight =draw.textsize(text=bidi_text,font=font,spacing=3,)
    print(txtlength, txtheight)
    # h,w += int(h*0.21)
    draw.multiline_text((((1080-txtlength)/2),((int(image.height)/2)-(txtheight/2))), bidi_text, (255,255,255), 
                        font=font,spacing=5, align='center',stroke_fill=(0,0,0), stroke_width= 1,)
    # sura = "{(الممتحنة - 4)}"
    sreshaped_text = reshaper.reshape(sura)    # correct its shape
    sbidi_text = get_display(sreshaped_text)           # correct its direction
    draw.multiline_text((((1080-txtlength)/2),(int(image.height -200))), sbidi_text, (255,255,255), font=font, spacing=2, align='center',stroke_fill=(0,0,0), stroke_width= 1, )
    # ImageDraw.Draw(image)
    # image = image.resize((1080,1080))
    # save it
    image.save('123.jpg')
# display(imge.resize((int(im.size[0]),int(im.size[1])), 0) )
def call_text():
    url = 'dua.html'
    soup = BeautifulSoup(open(url), 'lxml')
    print("\nFind and print all li tags:\n")
    for tag in soup.find_all("li")[:count]:
        # aya = tag.find("span")
        print("{0}: {1}".format(tag.name, tag.text))
            # print("{0}: {1}: {2}: {3}".format(tag.name, tag.text, aya.name, aya.text))
        # x, y = [tag.contents[1].contents[0], tag.contents[0]]
        
        # print(y)
    return tag #returns last in loop

def pexel_image():
    #tags used tag1+ tag2
    tag1 = ['space','moon','universe', 'stars', 'sky', 'autum', 'spring', 'winter', 'snow', 'mountain', 'jungle', 'ramadan', 'trees']
    tag2 = ['sunrise','dawn','night', 'noon', 'sun', 'twilight', 'dawning', 'aurora', 'landscape','blurred', 'outdoors']
    # tag3 = ['background','2040p','1080p','large','HD', 'wallpaper', ]
    text = (random.choice(tag1)) + " " +(random.choice(tag2))  #+ " " + (random.choice(tag3)
    # Create API object
    api = API(PEXELS_API_KEY)
    # Search five 'kitten' photos
    api.search(text, page=1, results_per_page=1)
    # Get photo entries
    photos = api.get_entries()
    # Loop the five photos
    for photo in photos:
      # Print photographer
      'Photographer: ', photo.photographer
      # Print url
      'Photo url: ', photo.url
      # Print original size url
      'Photo original size: ', photo.original
    response = requests.get(photo.original) # get photo
    if response.status_code == 200: # check gateway response
        with open(text+".jpg","wb") as file:
            file.write(response.content)
    print('--------------Image Saved')
    return str(text)

if __name__ == "__main__":
    create_image(imageFile=pexel_image(),texts=call_text())
    serial_code()
    print('---------Done----------')