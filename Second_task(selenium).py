
#за тегом
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome("C:/Users/Пользователь/Downloads/chromedriver_win32/chromedriver.exe")
browser.get("https://www.google.com.tr/search?q=automation+qa")

html_source = browser.page_source
value = browser.find_elements_by_link_text("habr.com")# find_element_by_xpath("//a[contains(text(), 'habr.com')]").click()
for elem in value:
    if value in html_source:
        print(value)
    else:
        print('false')

browser.close()