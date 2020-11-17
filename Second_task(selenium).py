

from selenium import webdriver
browser = webdriver.Chrome("C:/Users/Пользователь/Downloads/chromedriver_win32/chromedriver.exe")
browser.get("https://www.google.com.tr/search?q=automation+qa")

html_source = browser.page_source
for i in range(len(html_source) - 1):
    if "habr.com" in html_source:
        value = browser.find_element_by_css_selector("[class = 'yuRUbf']")
        print(value)
    else:
        print('false')

browser.close()