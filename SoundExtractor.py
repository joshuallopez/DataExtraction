####################################
# File name: scrapy.py             #
# Author: Josue Lopez L            #
# Last Update: 12/12/21            #
# Version: 0.0.1                   #
####################################


# Import the tools necessary to extract the url's content and regex through the data
# For the imports to work the modules must be installed in the machine you are running the program
import requests
from urllib.request import Request, urlopen
import re

# Set a max of pages based on the category (MyInstant Pagination)
maxPage = 15
# set the category to scrape from
category = 'voice'
# Go through all the pages from 1 to maxPage on the category
for i in range(1, maxPage):

    # Get all the links from page
    print('Page: (' + str(i) + '/' + str(maxPage) + ')')

    req = Request('https://www.myinstants.com/search/?page=1' +
                  str(i) + '&name=' + category, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode('utf-8')

    # Regex mp3 slug and store in resultsFile
    resultsFile = re.findall('<div class="small-button" onmousedown="play\\(\'(.*?)\'\)"></div>', webpage)
    resultsName = re.findall('class="instant-link">(.*?)</a>', webpage)
    counter = 0

    # Once all the sounds slugs are stored in resultsFile
    # Download all sounds from page to relative folder path ./sounds/
    for x in resultsFile:
        url = "https://www.myinstants.com" + x
        r = requests.get(url, allow_redirects=True)

        try:
            open('./sounds/' + resultsName[counter] +
                 ".mp3", 'wb').write(r.content)
        except:
            print('error download file')
            continue

        print(str(counter) + "- " + resultsName[counter] + " Downloaded")
        counter += 1