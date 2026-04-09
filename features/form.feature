Feature: Form Registration
  As a new user
  I want to fill the registration form
  So that I can register in the ToolsQA system

  Scenario: Successful registration by submitting a text file
    Given I access the Practice Form page
    When I fill out the entire form with random values
    And I submit the form
    Then a confirmation popup should be displayed
    And I close the popup