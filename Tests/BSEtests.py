from Modules.BSE_India import BSEactions


class BSEtests():
    def __init__(self, driver):
        self.driverInTest = driver
    def MyTest1(self):

        print('Test Execution starting...')
        BSEactions(self.driverInTest).LaunchBrowser("https://www.facebook.com")
        BSEactions(self.driverInTest).loginApp()

        print('Test Execution is success')
#add more tests here