from Generic.Base import baseForDriver
from Modules.BSE_India import BSEactions
from Tests.BSEtests import BSEtests

class BSEtestBatch(baseForDriver):
    def __init__(self):
        self.obj_driver = baseForDriver('CHROME').driver
    def CallTests(self):

        #self.driverInTest.get("https://www.facebook.com")
        #BSEactions(self.driverInTest).LaunchBrowser("https://www.facebook.com")
        BSEtests(self.obj_driver).MyTest1()
        #BSEtests(self.obj_driver).MyTest2()


BSEtestBatch().CallTests()