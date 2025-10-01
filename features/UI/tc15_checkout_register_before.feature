Feature: Place Order - Register before Checkout
  As a user
  I want to register before checkout
  So that I can complete my purchase

  Scenario: Register before checkout and place order
    Given I navigate to the home page
    When I click on Signup/Login link
    When I enter name and email for signup
    And I click Signup button
    When I fill account details
    And I fill address details
    And I click Create Account button
    Then I should see "ACCOUNT CREATED!" message
    When I click Continue button
    Then I should be logged in as the user
    When I click Products link
    And I add first product to cart
    And I click View Cart
    And I click Proceed To Checkout
    Then I should see checkout page
    And address details should be correct
    When I enter comment "Please handle with care"
    And I click Place Order
    When I enter payment details
    And I click Pay and Confirm Order
    Then I should see order success message
    When I click Delete Account link
    Then I should see "ACCOUNT DELETED!" message