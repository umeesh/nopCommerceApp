from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regresion
    def test_homepage_title(self, setup):
        self.logger.info('*********************Test_001_Login****************************')
        self.logger.info('*********************Verifying Home Page Title****************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('*********************Home Page Title Test is Passed****************************')
        else:
            self.driver.save_screenshot("../Screenshots/test_homepage_title.png")
            self.driver.close()
            self.logger.error('*********************Home Page Title Test is Failed****************************')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regresion
    def test_login(self, setup):
        self.logger.info('*******************Verifying Login Test****************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin("login")
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info('*********************Login Test is Passed****************************')
        else:
            self.driver.save_screenshot("../Screenshots/test_login.png")
            self.driver.close()
            self.logger.error('*********************Login Test is Failed****************************')
            assert False
