Feature: Contact Us Form
  As a user
  I want to submit contact us form
  So that I can get in touch with support

  Scenario: Submit contact us form
    Given I navigate to the home page
    When I click Contact Us link
    Then I should be on contact us page
    When I fill contact us form with name "John Doe" email "john@test.com" subject "Query" and message "Test message"
    And I upload a file
    And I click Submit button
    Then I should see contact form success message
    When I click Home button
    Then I should see the home page