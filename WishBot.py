from selenium import webdriver
import secrets, Wish_Paths, time

class WishBot:
    name = ""
    email = ""
    def __init__(self): #This init function logs in
        name = "temp"
        email = "temp@123.com"

    def login(self):
        driver = webdriver.Chrome(secrets.CHROMEDRIVER_PATH)
        driver.get("https://www.wish.com/")
        #Click (LOGIN WITH GOOGLE)
        clickButton = driver.find_element_by_xpath(Wish_Paths.LOGIN_GOOGLE_BUTTON)
        clickButton.click()
        time.sleep(2)

        #Username
        usernameField = driver.find_element_by_xpath(Wish_Paths.LOGIN_USERNAME_XPATH)
        usernameField.send_keys(secrets.WISH_EMAIL)
        
        #Password
        #passwordField = driver.find_element_by_xpath(Wish_Paths.LOGIN_PASSWORD_XPATH)
        #passwordField.send_keys(secrets.WISH_PASSWORD)

        while(1):
            name = ""


h = WishBot()
h.login()