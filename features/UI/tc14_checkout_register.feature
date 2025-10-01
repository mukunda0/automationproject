Feature: Place Order - Register while Checkout
  As a new user
  I want to register during checkout
  So that I can complete my purchase

  Scenario: Register during checkout and complete order
    Given I navigate to the home page
    When I click Products link
    And I add first product to cart
    And I click View Cart
    Then I should be on cart page
    When I click Proceed To Checkout
    And I click Register/Login from modal
    When I enter name and email for signup
    And I click Signup button
    When I fill account details
    And I fill address details
    And I click Create Account button
    Then I should see "ACCOUNT CREATED!" message
    When I click Continue button
    And I click Cart link
    And I click Proceed To Checkout
    Then I should see checkout page
    And address details should be correct
    When I enter comment "Please deliver between 9 AM - 5 PM"
    And I click Place Order
    When I enter payment details
    And I click Pay and Confirm Order
    Then I should see order success message
    When I click Delete Account link
    Then I should see "ACCOUNT DELETED!" message