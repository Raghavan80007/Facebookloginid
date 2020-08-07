import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.BaseClass import BaseClass
from PageObject.LoginPage import Login
from Data.LoginData import  LoginCredential

import time
class TestLogin(BaseClass):

     def test_fblogin(self,getData):
         log = self.getLogger()
         login = Login(self.driver)
         time.sleep(2)
         login.userID().send_keys(getData["username"])
         log.info("need to print userID")
         login.password().send_keys(getData["password"])
         log.info("Need to print the password")
         login.loginBtn().click()
         log.info("Click the button")


     @pytest.fixture(params= LoginCredential.testdata)
     def getData(self,request):
         return request.param




# pytest --html = report.html for taking reports.
#html file will be generated --> coply the file and paste it  in the url. it will show the record.