Feature: Progress Bar Validation
  As an automation evaluator
  I want to validate the Progress Bar behavior and dynamic controls
  To assure the ability to handle UI synchronization in Selenium

  Scenario: Control and Validate Progress Bar states
    Given I navigate to the "Progress Bar" page in the Widgets menu
    When I click the Start button and stop it before 25%
    Then I validate that the progress bar value is less than or equal to 25%
    When I click Start again to reach 100% and reset the progress bar