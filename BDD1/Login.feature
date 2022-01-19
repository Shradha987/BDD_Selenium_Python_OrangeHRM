@all

Feature: OrangeHRM Login
# Background:  Given I launch chrome browser
#    When I open orange hrm homepage
#    And Enter username "admin"
#    And Enter password "admin123"
#    And Click on login button
#    Then User must successfully login to the Dashboard Page

  Scenario: Login to OrnageHRM with valid parameters
    Given I launch chrome browser
    When I open orange hrm homepage
    And Enter username "admin"
    And Enter password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard Page


