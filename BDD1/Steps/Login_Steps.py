from behave import *
from selenium import webdriver

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome('Resources/chromedriver.exe')


@when('I open orange hrm homepage')
def openHomepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when('Enter username "{username}"')
def enterUsername(context,username):
    context.driver.find_element_by_name('txtUsername').send_keys('admin')




@when('Enter password "{password}"')
def enterUsername(context,password):
    context.driver.find_element_by_id('txtPassword').send_keys("admin123")


@when('Click on login button')
def loginButton(context):
    context.driver.find_element_by_id('btnLogin').click()


@then('User must successfully login to the Dashboard Page')
def dashboardPage(context):
    val = context.driver.find_element_by_xpath('//div[@class="head"]').text
    assert val == "Dashboard"
    # context.driver.close()




# @given('I launch chrome browser')
# def launchBrowser(context):
#     context.driver = webdriver.Chrome('Resources/chromedriver.exe')
#
#
# @when('I open orange hrm homepage')
# def openHomepage(context):
#     context.driver.get('https://opensource-demo.orangehrmlive.com/')
#
#
# @when('Enter username "{username}"')
# def enterUsername(context,username):
#     context.driver.find_element_by_name('txtUsername').send_keys('admin')
#
#
#
#
# @when('Enter password "{password}"')
# def enterUsername(context,password):
#     context.driver.find_element_by_id('txtPassword').send_keys("admin123")
#
#
# @when('Click on login button')
# def loginButton(context):
#     context.driver.find_element_by_id('btnLogin').click()
#
#
# @then('User must successfully login to the Dashboard Page')
# def dashboardPage(context):
#     val = context.driver.find_element_by_xpath('//div[@class="head"]').text
#     assert val == "Dashboard"
#
# @then(u'navigate to Admin button')
# def step_impl(context):
#     context.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b').click()
#
#
# @then(u'click on User Management')
# def step_impl(context):
#     context.driver.find_element_by_xpath('//*[@id ="menu_admin_UserManagement"]').click()
#
#
# @then(u'click on Users')
# def step_impl(context):
#     pass