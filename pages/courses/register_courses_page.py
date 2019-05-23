import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_field = "search-courses"
    _course = "JavaScript for beginners"
    _enroll_button = "enroll-button"
    _cc_number = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvv"
    _submit_enroll = "//label[@for='spc-primary-submit']"
    _enroll_error_message = "//div[@class='cc__error alert-danger']"


    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_number)

    def enterCardExp(self, exp):
       self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv)

    def clickEnrollSubmitButton(self):
        self.sendKeys(self._submit_enroll, locator="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result