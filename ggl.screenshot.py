from selenium import webdriver
import time

wd = webdriver.Chrome()

wd.get('https://www.google.com')

time.sleep(3) # pause so the user can see and enjoy

wd.save_screenshot('ggl.screenshot.png')

wd.quit()
