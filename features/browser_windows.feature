Feature: Browser Windows Handling
  As a user
  I want to interact with multiple browser windows
  To verify that the application opens new content correctly

  Scenario: Validate message in a new window
    Given I access the "Browser Windows" page
    When I click on the "New Window" button
    Then a new window should open with the message "This is a sample page"
    And I close the new window