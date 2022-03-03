from ObjRepo.repoBSEIndia import bseRepo
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions #as EC

class UIactions():
    def __init__(self, objDriver):
        self.driverInUI = objDriver
    def typeIntextBox(self, sInput):
        print('typing in text box')
        bseRepo().objRepoPage1()
        print(bseRepo().objRepoPage1.element1)
        print(bseRepo().objRepoPage1.element2)

        element = self.driverInUI.find_element(by=By.ID, value='email')
        element.send_keys(sInput)


        time.sleep(4)

        #Develop selenium methods here
        print('typing in text box is success')
    def verifycombo(self):
        pass