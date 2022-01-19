from behave import *
from selenium import webdriver

@then(u'navigate to Admin button')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b').click()


@then(u'click on User Management')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id ="menu_admin_UserManagement"]').click()


@then(u'click on Users')
def step_impl(context):
    pass