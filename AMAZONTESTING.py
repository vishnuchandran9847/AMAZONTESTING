
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\chrome23\\chromedriver.exe")
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
time.sleep(4)
driver.maximize_window()

#AMAZON LOGIN OF THE CUSTOMER

login=driver.find_element(by=By.ID,value="ap_email").send_keys("vishnualexa112@gmail.com")
signin=driver.find_element(by=By.ID,value="continue").click()
password=driver.find_element(by=By.ID,value="ap_password").send_keys("Vishnu@121")
submit=driver.find_element(by=By.ID,value="signInSubmit").click()

#TO SEARCH THE ITEM WE WANT

def searchbox():
    time.sleep(4)
    search=driver.find_element(by=By.ID,value="twotabsearchtextbox").send_keys("shirts for men")
    click=driver.find_element(by=By.XPATH,value="//*[@id='nav-search-submit-button']").click()
searchbox()
time.sleep(5)
driver.get("https://www.amazon.com/s?k=shirts+for+men&crid=180H4YV40V6Z9&sprefix=shirt%2Caps%2C463&ref=nb_sb_ss_ts-doa-p_2_5")
#find=driver.find_element(by=By.XPATH,value="//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div[1]/h2/a")
find=driver.find_element(by=By.LINK_TEXT,value="Legendary Whitetails Men's Buck Camp Flannel Shirt")
find.click()
detail_of_shirt=driver.find_element(by=By.ID,value="title")
print("detail of shirt:",detail_of_shirt.text)
time.sleep(4)

#SELECTED ITEM IS ADDED TO ADD TO CART

add_tocart=driver.find_element(by=By.ID,value="add-to-cart-button")
add_tocart.click()
time.sleep(4)

#TO CHECK GIFT CARDS

gift_cards=driver.find_element(by=By.LINK_TEXT,value="Gift Cards")
gift_cards.click()
time.sleep(4)
see_all_giftcards=driver.find_element(by=By.LINK_TEXT,value="See all occasions")
see_all_giftcards.click()
#birthday_to_play=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div[2]/span/a/div/img")
#birthday_to_play.click()

#HERE WE GO BACK TO THE WINDOW

driver.back()
driver.get("https://www.amazon.com/gp/cart/view.html/ref=sw_rv_inscr?app-nav-type=none&dc=df")
time.sleep(4)

#GOES TO PROCCED THE ITEM,WANT TO PURCHASE THE ITEM

proceed_to_check=driver.find_element(by=By.NAME,value="proceedToRetailCheckout").click()
driver.get("https://www.amazon.com/gp/buy/payselect/handlers/display.html?_from=cheetah")
time.sleep(3)

#PLACE AND LOCATION OF THE CUSTOMER

place=Select(driver.find_element(by=By.XPATH,value="//*[@id='address-ui-widgets-countryCode-dropdown-nativeId']"))
place.select_by_visible_text("India")
india_to_display=driver.find_element(by=By.LINK_TEXT,value="India").click()

full_name=driver.find_element(by=By.ID,value="address-ui-widgets-enterAddressFullName")
full_name.send_keys("vishnualexa")
time.sleep(3)

#TO CHECK ADDRESS AND MORE DETAILS OF THE CUSTOMER

address=driver.find_element(by=By.CSS_SELECTOR,value="input#address-ui-widgets-enterAddressLine1")
address.send_keys("Alexander General Delivery    ")
address_location=driver.find_element(by=By.CSS_SELECTOR,value="input#address-ui-widgets-enterAddressLine2")
address_location.send_keys("PORT ALEXANDER,206 MAINST")
city=driver.find_element(by=By.CSS_SELECTOR,value="input#address-ui-widgets-enterAddressCity")
city.send_keys("malappuram")
state=driver.find_element(by=By.ID,value="address-ui-widgets-enterAddressStateOrRegion")
state.send_keys("kerala")
zipode=driver.find_element(by=By.ID,value="address-ui-widgets-enterAddressPostalCode")
zipode.send_keys("676503")
phone_number=driver.find_element(by=By.ID,value="address-ui-widgets-enterAddressPhoneNumber")
phone_number.send_keys("7907394963")
time.sleep(4)
checkox=driver.find_element(by=By.ID,value="address-ui-widgets-use-as-my-default").click()
use_address=driver.find_element(by=By.CLASS_NAME,value="a-button-input").click()
time.sleep(3)

#HERE WE TO CHECK ADD TO ANOTHER ACCOUNT AND EDIT ADDRESS

change_address=driver.find_element(by=By.ID,value="addressChangeLinkId")
change_address.click()





















