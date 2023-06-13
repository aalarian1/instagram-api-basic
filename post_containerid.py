from defines import getCreds, makeApiCall
import requests


def PostContainerID(params):
    # """ Get instagram account

    # API Endpoint:
    # ""
    # 	graph.facebook.com/17841400008460056/media?image_url=https//www.example.com/images/bronzed-fonzes.jpg
    #                                                 & caption= #BronzedFonzes!
    #                                                  & user_tags=
    # Returns:
    # 	object: data from the endpoint
    # """

    endpointParams = dict()  # parameter to send to the endpoint
    # tell facebook we want to exchange token
    endpointParams['caption'] = '123.jpg'  # access token
    endpointParams['image_url'] = '123.jpg'  # access token
    endpointParams['location-id'] = '123.jpg'  # access token
    endpointParams['user-tags'] = '123.jpg'  # access token
    endpointParams['access_token'] =  params['access_token']

    # endpointParams['access_token'] = params['access_token']
    # endpointParams['caption']  = "#bEsmlla" # caption
    url = params['endpoint_base'] + params['instagram_account_id'] +'/media? '  # endpoint url

    # makeApiCall( url, endpointParams, params['debug'] ) # make the api call
    return requests.post(url, endpointParams, params['debug'])


params = getCreds()  # get creds
params['debug'] = 'yes'  # set debug
response = PostContainerID(params)  # get debug info

print(response.json())

# print ("\n---- INSTAGRAM ACCOUNT INFO ----\n")
# print ("Page Id:") # label
# print( response['json_data']['id'] )# display the page id
# print( "\nInstagram Business Account Id:" )# label
# print( response['json_data']['instagram_business_account']['id'] )#display the instagram account id
# # url = ' https://graph.facebook.com/me/media?image_url=https//www.example.com/images/bronzed-fonzes.jpg&caption=#BronzedFonzes!&location-id=(Cairo, Egypt)'
# # print(requests.post(url).json())