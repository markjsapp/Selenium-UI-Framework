Feature: Google Search

  Scenario: Search for Selenium
    Given I am on the Google homepage
    When I search for "Selenium"
    Then the search results should contain "Selenium"