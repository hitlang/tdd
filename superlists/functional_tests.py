#测试驱动开发
from selenium import  webdriver


browser = webdriver.Firefox()

browser.get("http://localhost:8000") # 网址


assert  'Django' in browser.title


browser.close()