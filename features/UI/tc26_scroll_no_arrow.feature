Feature: Verify Scroll Up without using Arrow button
  As a user
  I want to scroll to top manually
  So that I can navigate without arrow button

  Scenario: Scroll to bottom and back to top without arrow
    Given I navigate to the home page
    When I scroll to bottom of page
    Then I should see SUBSCRIPTION at footer
    When I scroll up to top
    Then I should see full-fledged text