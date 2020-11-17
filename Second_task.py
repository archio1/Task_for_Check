import webbrowser

import lxml.html
from bs4 import BeautifulSoup
import requests
import urllib
from urllib.request import urlopen
import time
from html.parser import HTMLParser

# while True:
#     try:
openUrl = BeautifulSoup(urlopen("https://www.google.com.tr/search?q=automation+qa").read)
print("result code:" + str(openUrl.getcode()))
    #     break
    #
    # except Exception as e:
    #     print(e)


soup = BeautifulSoup(openUrl, 'habr.com')

print(soup.h2)
print(soup.head)
print(soup.li)
print(soup.title)

# class TitleParser(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.match = False
#         self.title = ''
#
#     def handle_starttag(self, tag, attributes):
#         self.match = True if tag == 'title' else False
#
#     def handle_data(self, data):
#         if self.match:
#             self.title = data
#             self.match = False
#
# url = "https://www.google.com.tr/search?q=automation qa"
# html_string = str(urlopen(url).read())
#
# parser = TitleParser()
# parser.feed(html_string)
# print(parser.title)


#response = requests.get(
#    'https://www.google.com.tr/search?q=automation qa',
#    params={'q': 'habr.com'},
#)

#json_response = response.json()
#repository = json_response['items'][0]
#print(f'Title: {repository["name"]}')


# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )
#
# # просмотр нового массива `text-matches` с предоставленными данными
# # о поиске в пределах результатов
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Text matches: {repository["text_matches"]}')


# webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
# webbrowser.get('Chrome').open_new_tab('https://www.google.com.tr/search?q=automation qa')
#


#
# soup = BeautifulSoup(urlopen("https://www.google.com").read)
# print(soup.title.string)

# url = 'https://www.google.com.tr/search?q=automation qa'
# html_string = str(urlopen(url).read())
#
# t = lxml.html.parse(url)
# #
# #
# titles = t.find("habr.com").text
# #
# print(titles)

## Google Search query results as a Python List of URLs
##search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

#webbrowser.open('https://www.google.com/', new=2)
#webbrowser.open_new_tab('https://www.google.com/search/?text=' + 'automation qa')

#webbrowser.get('chrome').open('g')
