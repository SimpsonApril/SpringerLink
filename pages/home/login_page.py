import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "» Sign up / Log in"
    _email_field = "login-box-email"
    _password_field = "login-box-pw"
    _login_button = "Log in"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="title")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("user")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Unfortunately the details you "
                                       "supplied do not match our records. Please check and try again')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Home - Springer")