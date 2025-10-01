Feature: Verify Test Cases Page
  As a user
  I want to navigate to test cases page
  So that I can view all available test cases

  Scenario: Navigate to test cases page
    Given I navigate to the home page
    Then I should see the home page
    When I click Test Cases link
    Then I should be on test cases page