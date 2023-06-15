# Quran Quotes Instagram Bot

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Platform](https://img.shields.io/badge/Platform-Instagram-lightgrey)

Instagram Quran Quotes Posting Bot is a Python-based tool for automating the process of posting Quran quotes as text overlays on royalty-free images to Instagram. This project is aimed at reducing the time and effort needed for manual postings, enabling you to focus on other valuable aspects of your project or business. These posts will comprise of royalty-free images overlaid with inspiring quotes from the Quran, which are automatically posted to Instagram using the Instagram Graph API.

This repository contains all the necessary scripts for fetching quotes, processing images, creating text overlays, and publishing to Instagram via the Instagram Graph API.


## Features
- Fetching beautiful royalty-free images from Unsplash API.
- Overlaying Quranic verses onto these images using the Pillow library in Python.
- Automating Instagram posts using Instagram's Graph API.

## Prerequisites

Ensure you have the following installed on your local machine:
#### requirments.txt
  ```
  # common libraries in Python projects
  numpy
  pandas
  matplotlib
  scipy
  # if you're using requests
  requests
  # if you're using BeautifulSoup
  beautifulsoup4
  # if you're using selenium
  selenium
  # replace and add with your project specific libraries
  ```
You will also need the following API Keys:
  ```
  - PEXELS_API_KEY (Pexels)
  - UNSPLASH_API_KEY and UNSPLASH_SECRET_KEY (Unsplash)
  - FB_APP_CLIENT_ID and FB_APP_CLIENT_SECRET (Facebook App)
  - ACCESS_TOKEN (Instagram)
  - FB_PAGE_ID and INSTAGRAM_BUSINESS_ACCOUNT_ID (Facebook Page and Instagram Business Account respectively)
  ```
## Installation & Usage

1. Clone this repository and navigate to the project directory.
    ```
    git clone <repository_url>
    cd <repository_directory>
    ```
    
2. Install necessary dependencies.
    ```
    pip install -r requirements.txt
    ```

3. Edit the `config.py` file and fill it with your own API keys and Access Tokens.

4. Run the main script.
    ```
    python main.py
    ```
## Directory Structure
The repository contains the following main Python files:

The scripts do the following:

Scrape images from Google Image Search.
Fetch Quran quotes.
Overlay the quotes on the images.
Get long-lived access tokens from Facebook's Graph API.
Get user media and page information.
Post the created content to an Instagram account.
These functionalities are implemented in multiple Python scripts.

Here is a basic outline of the project's directory structure and the role of each file:

- `amazon-keyword.py`: Contains functionality related to Amazon keywords.
- `business_discovery.py`: Handles business-related data discovery.
- `config.py`: Contains configuration details, possibly for the entire project or a specific module.
- `count.py`: Likely contains functions related to counting some form of data.
- `debug_access_token.py`: Contains code to debug issues with access tokens.
- `defines.py` & `defines_py3.py`: Define various constants or settings used across the project.
- `get_instagram_account.py`: Contains code to fetch details of an Instagram account.
- `get_long_lived_access_token.py`: Handles the retrieval of long-lived access tokens.
- `get_user_media.py`: Fetches media associated with a user account.
- `get_user_pages.py`: Fetches the pages associated with a user account.
- `Imagedraw.py`: Contains code related to drawing or modifying images.
- `imagescrapper.py` & `imagescrapper copy.py`: Scrapes images from specified locations.
- `php/posting_content.php`: Contains PHP code for posting content.
- `post_containerid.py`: Handles actions related to container ids in posts.
- `publishing.py`: Contains code related to publishing posts.
- `serialcode.py`: Likely related to the generation or handling of serial codes.
- `test_publish_tutorial.py`: Code to test publishing tutorials.
- `text.py`: Likely contains functions related to text processing.
- `unsplash.py`: May contain code related to Unsplash, possibly image scraping or API communication.
- `fetching.py`: Fetches quotes from the API and processes the JSON response.
- `image_processing.py`: Fetches images from a public URL, adds a text overlay to them, and saves them to the local machine.
- `publishing.py`: Utilizes the Instagram Graph API to create a media object, check its status, and publish the media on Instagram.
- `serialcode.py`: Generates and maintains a count of the number of times the program is called.
- `test_publish_tutorial.py`: Tests the publishing functionality of the bot.
- `defines_py3.py`: Contains necessary credentials and parameters needed for the Instagram API calls.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
This project is developed for educational purposes. Be aware of the rules and policies of Instagram regarding automated posts. The developers of this project are not responsible for any misuse of this project.

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for additional details.

## Authors
- Ahmed Alarian (https://github.com/aalarian1)

## Acknowledgements
A big thank you to the communities behind the APIs and libraries used in this project.
