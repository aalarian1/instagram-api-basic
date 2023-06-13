# # importing google_images_download module
# from google_images_download import google_images_download 
  

from selenium import webdriver
import time, requests


# def search_google():#(search_query)
browser = webdriver.Chrome(executable_path=r'/Users/macbookair/Downloads/chromedriver')
search_url = f"https://www.pexels.com/search/dawn%20sky%201080px1080p/"
images_url = []
# open browser and begin search
browser.get(search_url)
elements = browser.find_elements_by_class_name('photo-item')

APIIII
count = 0
for e in elements:
    # get images source url
    e.click()
    pht = browser.find_elements_by_class_name('rd__button-group')
    # images_url.append(pht[0].get_attribute("src"))
    tag = "dawn sky 1080x1080p"
    # dw =pht[0].find_element_by_partial_link_text('Conti')
    pht[0].click()
    # reponse = requests.get(images_url[0])
    # if reponse.status_code == 200:
    #     with open(f"search{tag+1}.jpg","wb") as file:
    #         file.write(reponse.content)
    # time.sleep(1)
    
    #     element = browser.find_elements_by_class_name('v4dQwb')

    #     # Google image web site logic
    #     if count == 0:
    #         big_img = element[0].find_element_by_class_name('n3VNCb')
    #     else:
    #        big_img = element[1].find_element_by_class_name('n3VNCb') #these only work for dogs change

    #     images_url.append(big_img.get_attribute("src"))

    #     # write image to file
    #     reponse = requests.get(images_url[count])
    #     if reponse.status_code == 200:
    #         with open(f"search{count+1}.jpg","wb") as file:
    #             file.write(reponse.content)

    #     count += 1

    #     # Stop get and save after 5
    #     if count == 5:
    #         break

    # return images_url
# items = search_google()
