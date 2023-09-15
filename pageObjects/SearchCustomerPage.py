from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchCustomer:

    SearchEmail_id = 'SearchEmail'
    SearchFirstName_id = "//input[@id='SearchFirstName']"
    SearchLastName_id = "//input[@id='SearchLastName']"
    SearchButton_id = "//button[@id='search-customers']"

    SearchTable_xpath = "//table[@id='customers-grid']"
    SearchTableRow_xpath = "//table[@id='customers-grid']//tbody/tr"
    SearchTableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.SearchEmail_id).clear()
        self.driver.find_element(By.ID, self.SearchEmail_id).send_keys(email)

    def SetFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.SearchFirstName_id).clear()
        self.driver.find_element(By.XPATH, self.SearchFirstName_id).send_keys(firstname)

    def SetLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.SearchLastName_id).clear()
        self.driver.find_element(By.XPATH, self.SearchLastName_id).send_keys(lastname)

    def ClickSearchButton(self):
        self.driver.find_element(By.XPATH, self.SearchButton_id).click()

    def getNoofRow(self):
        return len(str(self.driver.find_element(By.XPATH, self.SearchTableRow_xpath)))

    def getNoofColumn(self):
        return len(self.driver.find_element(By.XPATH, self.SearchTableColumn_xpath))

    def SearchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoofRow() + 1):
            table = self.driver.find_element(By.XPATH, self.SearchTable_xpath)
            emai_lid = table.find_element(By.XPATH,
                                                "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if email == emai_lid:
                flag = True
                break
        return flag

    def SearchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoofRow() + 1):
            table = self.driver.find_element(By.XPATH, self.SearchTable_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text

            if name == Name:
                flag = True
                break
        return flag
