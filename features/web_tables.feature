Feature: Web Tables Management
  As an automation engineer
  I want to interact with the Web Tables application
  So that I can add, edit, and delete user records successfully

  Scenario: Add, Edit and Delete a single record in Web Tables
    Given I access the Web Tables page
    When I create a new record with random data
    Then the new record should be visible in the table
    When I edit the newly created record with new random data
    Then the updated record should be visible in the table
    When I delete the current record
    Then the record should no longer be visible in the table