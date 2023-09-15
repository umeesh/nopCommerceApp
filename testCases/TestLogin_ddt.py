import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = '../TestData/LoginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regresion
    def test_login_ddt(self, setup):
        self.logger.info('******************* Test_002_DDT_Login ****************************')
        self.logger.info('*******************Verifying Login Test****************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('number of rows i a excel', self.rows)

        lst_status = []  # EMPTY LIST

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin('login')
            time.sleep(5)
            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*****PASSED****")
                    self.lp.clickLogout('logout')
                    lst_status.append("PASS")
                elif self.exp == 'Fail':
                    self.logger.info("*****Failed1****")
                    self.lp.clickLogout('logout')
                    lst_status.append("Fail")
                    time.sleep(5)

            if act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*****Failed****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("*****passed****")
                    lst_status.append("pass")
                    time.sleep(5)

        if "Fail" not in lst_status:
            self.logger.info("************LOGIN DDT Test Passed******************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****************LOGIN DDT Test Failed*************")
            self.driver.close()
            assert False
        self.logger.info("************END OF THE LOGIN DDT Test******************")
        self.logger.info("***********LOGIN 002 DDT COMPLETED*******************")
