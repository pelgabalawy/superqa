import pytest
from selenium import webdriver
from seleniumpagefactory.Pagefactory import PageFactory


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

    pglogin = LoginPage(driver)
    pglogin.login()

class LoginPage(PageFactory):

    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        super().__init__()
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]'),
        "lnkPost": ('XPATH', '//div[contains(text(),"Posts")]'),
        "lstAction": ('ID', 'bulk-action-selector-top')
    }

    def login(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text("opensourcecms")               # edtUserName become class variable using PageFactory
        self.edtPassword.set_text("opensourcecms")
        self.btnSignIn.click_button()