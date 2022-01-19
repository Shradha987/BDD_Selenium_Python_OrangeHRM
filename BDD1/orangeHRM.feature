@all

Feature: OrangeHRM Logo

  @all
  Scenario: Logo presence on OrangeHRM home Page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo is present on page
    And I close browser