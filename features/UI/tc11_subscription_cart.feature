Feature: Verify Subscription in Cart Page
  As a user
  I want to subscribe from cart page
  So that I can receive updates

  Scenario: Subscribe to newsletter from cart page
    Given I navigate to the home page
    When I click Cart link
    When I scroll down to footer on cart page
    Then I should see SUBSCRIPTION text
    When I enter email "cart@subscription.com" and click subscribe on cart
    Then I should see subscription success on cart