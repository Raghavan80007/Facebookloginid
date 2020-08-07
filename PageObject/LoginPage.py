from selenium.webdriver.common.by import By

class Login:

    def __init__(self,driver):
        self.driver = driver

    Userid = (By.ID,"email")
    pwd    = (By.ID,"pass")
    logindID = (By.XPATH,"//input[@value='Log In']")

    def userID(self):

        return self.driver.find_element(*Login.Userid)


    def password(self):

        return self.driver.find_element(*Login.pwd)

    def loginBtn(self):

        return self.driver.find_element(*Login.logindID)

