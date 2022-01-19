from behave import *
from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome('Resources/chromedriver.exe')


@when('open orange hrm homepage')
def openHomepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@then('verify that the logo is present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath('//div[@id="divLogo"]')
    if status:
        print('True')
    # assert status == True


@then('I close browser')
def closeBrowser(context):
    context.driver.close()