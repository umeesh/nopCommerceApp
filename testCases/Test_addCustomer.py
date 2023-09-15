import random
import string

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer


def random_generator():
    pass


class Test_003_addCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regresion
    def test_addCustomer(self, setup):
        self.logger.info('*********************Test_003_AddCustomer****************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin("login")
        self.logger.info('*********************Login Successful****************************')

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomerMenu()
        self.addCust.clickCustomerItem()
        self.addCust.ButtonAddNew()
#
        self.logger.info("**************Providing Customer Info********************************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.SetEmail(self.email)
        self.addCust.SetPassword("Aria@123")
        self.addCust.SetFirstName("Aria")
        self.addCust.SetLastName("Pathak")
        self.addCust.SetDOB("12/01/2023")  # format: DD/MM/YYYY
        self.addCust.SetGender("Female")
        self.addCust.SetCompanyName("UmeshQA")
        self.addCust.SetNews_Letter("Test store 2")
        self.addCust.SetCustomerRoles("Forum Moderators")
        self.addCust.SetManagerOfVendor("Vendor 2")
        self.addCust.SetAdminComment("This is my first Automation Project....")
        self.addCust.clickTax()
        self.addCust.clickSaveButton()
        self.logger.info("*************************Saving Customer Info *************************")
        self.logger.info("*************************Customer Validation Started *************************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*************************Customer Test Passed *************************")
        else:
            self.driver.save_screenshot('../Screenshots/Add_Customer_Screenshot.png')
            self.logger.error("************************* Test Case Failed *************************")
        self.driver.close()
        self.logger.info("********************Ending the home page title text******************************")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



