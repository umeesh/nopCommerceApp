from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()

    return driver

# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome Browser.........")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox Browser..........")
#     return driver
#
#
# #
#
# def pytest_addoption(parser):  # This will get value from CLI/hooks
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):  # This will return the browser value to setup method
#     return request.config.getoption("--browser")
#
#
# ###################### PYTEST HTML REPORTS####################################
# It is hook for adding environment info to the HTML Report.
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Module Name'] = 'Customer'
#     config._metadata['Tester'] = 'Umesh'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
