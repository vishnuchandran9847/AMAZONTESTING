from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\chrome23\\chromedriver.exe")
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# Form of tutorial page
driver.maximize_window()
first_name=driver.find_element(by=By.NAME,value="firstname").send_keys("vishnu")
last_name=driver.find_element(by=By.NAME,value="lastname").send_keys("chandran")
#gender=driver.find_element(by=By.XPATH,value="//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[3]/td[2]/input[1]").click()
#year_experience=driver.find_element(by=By.XPATH,value="//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[4]/td[2]/span[1]/input").click()
date=driver.find_element(by=By.XPATH,value="//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[5]/td[2]/input").send_keys("20/10/22")
profession=driver.find_element(by=By.XPATH,value="//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[6]/td[2]/span[2]/input").click()
uploadpicture=driver.find_element(by=By.NAME,value="photo").send_keys("D:/baby.jpg")