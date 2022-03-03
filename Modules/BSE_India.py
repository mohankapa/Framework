from UserActions.UIactions import UIactions



class BSEactions():
    def __init__(self, driver):
        self.driverInActions = driver
    def LaunchBrowser(self, surl):
        print('Launch browser action execution starting...')
        self.driverInActions.get("https://www.facebook.com")
        print('Launch browser action ending')
    def loginApp(self):
        print('LoginApp action execution starting...')
        UIactions(self.driverInActions).typeIntextBox('MyUserName')
        print('LoginApp action ending')

# add more business actions here