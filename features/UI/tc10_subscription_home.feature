Feature: Verify Subscription in Home Page
  As a user
  I want to subscribe to newsletter
  So that I can receive updates

  Scenario: Subscribe to newsletter from home page
    Given I navigate to the home page
    Then I should see the home page
    When I scroll down to footer
    Then I should see SUBSCRIPTION text
    When I enter email "test@subscription.com" and click subscribe
    Then I should see success subscription message