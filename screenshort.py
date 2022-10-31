import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
driver=webdriver.Chrome(executable_path="C:\\chrome23\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.save_screenshot("ss.png")
screenshot=Image.open("ss.png")
screenshot.show()