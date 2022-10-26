import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\chrome23\\chromedriver.exe")
driver.get("https://www.google.com/maps/@10.54063,76.1283185,7z")
time.sleep(3)
def searchplace():
    search=driver.find_element(by=By.CLASS_NAME,value="tactile-searchbox-input").send_keys("kochin")
    submit=driver.find_element(by=By.XPATH,value="//*[@id='searchbox-searchbutton']").click()
searchplace()
driver.maximize_window()
def directions():
    time.sleep(7)
    direction=driver.find_element(by=By.XPATH,value="//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button").click()
directions()
def find():
    time.sleep(5)
    start_point=driver.find_element(by=By.XPATH,value="//*[@id='sb_ifc51']/input").send_keys("kozhikkode")
    time.sleep(5)
    search=driver.find_element(by=By.XPATH,value="//*[@id='directions-searchbox-0']/button[1]").click()
find()
def kilometers():
    time.sleep(5)
    total_kilometers=driver.find_element(by=By.XPATH,value="//*[@id='section-directions-trip-0']/div[1]/div[1]/div[1]/div[2]/div")
    print("total kilometers:",total_kilometers.text)
    time.sleep(5)
    train=driver.find_element(by=By.XPATH,value="//*[@id='section-directions-trip-1']/div[1]/div[2]/div[1]/div")
    print("train travel:",train.text)
kilometers()



