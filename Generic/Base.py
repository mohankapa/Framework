import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#from webdriver_manager.firefox import import fir
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions #as EC

class baseForDriver():
    def __init__(self, sBrowser):

        match sBrowser:
            case 'CHROME':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            case 'EDGE':self.driver = webdriver.edge(service=Service(ChromeDriverManager().install()))