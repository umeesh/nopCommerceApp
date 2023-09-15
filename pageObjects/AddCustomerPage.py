import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:  # add customer page

    linkCustomers_menu_xpath = "//i[@class = 'nav-icon far fa-user']"
    linkCustomer_item_xpath = "//a[@href='/Admin/Customer/List']"
    bttnAddNew_xpath = "//i[@class='fas fa-plus-square']"
    text_email_name = "//input[@id='Email']"
    text_password_id = "//input[@id='Password']"
    text_firstname_id = "//input[@id='FirstName']"
    text_lastname_id = "//input[@id='LastName']"
    radio_genderMale_id = "Gender_Male"
    radio_genderFemale_id = "Gender_Female"
    date_DateOfBirth_xpath = "//input[@id='DateOfBirth']"
    text_CompanyName_xpath = "//input[@id='Company']"
    check_istaxExempt_xpath = "//label[@for='IsTaxExempt']"
    xpath_news_letter = "//input[@aria-labelledby='SelectedNewsletterSubscriptionStoreIds_label']"
    xpath_opt1_News = "//li[normalize-space()='Your store name']"
    xpath_opt2_News = "//li[normalize-space()='Test store 2']"
    txtCustomerRole_xpath = "//div[@class = 'k-multiselect-wrap k-floatwrap']"
    lstitemAdminRole_xpath = "//li[normalize-space()='Administrators']"
    lstItemModeratorRole_xpath = "//li[normalize-space()='Forum Moderators']"
    lstItemGuestRole_xpath = "//li[normalize-space()='Guests']"
    lstItemRegisteredRole_xpath = "//li[normalize-space()='Registered']"
    textManagerofVendor_xpath = "//select[@id='VendorId']"
    # checkboxActive_xpath = "//input[@id='Active']"
    textarea_xpath = "//textarea[@id='AdminComment']"
    button_save_xpath = "//button[@name='save']"
    button_saveandcontinue_xpath = "//button[@name='save-continue'"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomers_menu_xpath).click()

    def clickCustomerItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_item_xpath).click()

    def ButtonAddNew(self):
        self.driver.find_element(By.XPATH, self.bttnAddNew_xpath).click()

    def SetEmail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_name).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_id).send_keys(password)

    def SetFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.text_firstname_id).send_keys(firstname)

    def SetLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.text_lastname_id).send_keys(lastname)

    def SetGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.radio_genderMale_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.radio_genderFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_genderMale_id).click()

    def SetDOB(self, dob):
        self.driver.find_element(By.XPATH, self.date_DateOfBirth_xpath).send_keys(dob)

    def SetCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.text_CompanyName_xpath).send_keys(company)

    def clickTax(self):
        self.driver.find_element(By.XPATH, self.check_istaxExempt_xpath).click()

    def SetNews_Letter(self, news):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_news_letter).click()

        if news == 'Test store 2':
            self.listitem = self.driver.find_element(By.XPATH, self.xpath_opt2_News)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.xpath_opt1_News)

    def SetCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRole_xpath).click()
        time.sleep(2)
        if role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdminRole_xpath)
        elif role == 'Registered':
            self.driver.find_element(By.XPATH, self.lstItemRegisteredRole_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemGuestRole_xpath)

        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemModeratorRole_xpath)

        elif role == 'Vendor':
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemVendorRole_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstItemGuestRole_xpath)
        #
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    #
    def SetManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.textManagerofVendor_xpath))
        drp.select_by_visible_text(value)

    #
    # def ClickActive(self):
    #     self.driver.find_element(By.XPATH, self.checkboxActive_xpath).click()
    #
    def SetAdminComment(self, content):
        self.driver.find_element(By.XPATH, self.textarea_xpath).send_keys(content)

    def clickSaveButton(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
        time.sleep(5)
