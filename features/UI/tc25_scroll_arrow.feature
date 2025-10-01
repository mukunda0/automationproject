Feature: Verify Scroll Up using Arrow button
  As a user
  I want to scroll to top using arrow button
  So that I can quickly navigate to top

  Scenario: Scroll to bottom and back to top using arrow
    Given I navigate to the home page
    When I scroll to bottom of page
    Then I should see SUBSCRIPTION at footer
    When I click scroll up arrow
    Then page should be scrolled to top