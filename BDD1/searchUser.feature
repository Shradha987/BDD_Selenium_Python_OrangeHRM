# Created by admin at 19/01/2022
Feature:Search User
  # Enter feature description here

  Scenario: Search User
    Given I launch chrome browser
    When I open orange hrm homepage
    And Enter username "admin"
    And Enter password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard Page
    And navigate to Admin button
    And click on User Management
    Then click on Users
