Feature: Sortable List Validation
  As an automation evaluator
  I want to validate drag and drop capabilities
  To ensure UI element manipulation is handled correctly

  Scenario: Sort list elements in ascending order
    Given I navigate to the "Sortable" page
    When I reorder the list into ascending order using drag and drop
    Then I validate that the list is in ascending order