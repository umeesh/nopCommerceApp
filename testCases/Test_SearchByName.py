import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_SearchCustByname_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regresion
    def test_SearchCustByName(self, setup):
        self.logger.info('*********************Search Customer By Email Test_004****************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin("login")
        self.logger.info('*********************Login Successful****************************')

        self.logger.info('*********************Add Customer Started*******************')
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomerMenu()
        self.addCust.clickCustomerItem()
        self.logger.info('*********************Search Customer By Name is Started*******************')

        self.SearchCust = SearchCustomer(self.driver)
        self.SearchCust.SetFirstName("Arthur")
        self.SearchCust.ClickSearchButton()

        time.sleep(7)
        status = self.SearchCust.SearchCustomerByName("Arthur Holmes")
        assert True == status
        self.logger.info('*******************Search Customer By Name Test_005 Finished*********************')
