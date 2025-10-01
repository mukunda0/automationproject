Feature: Place Order - Login before Checkout
  As a registered user
  I want to login before checkout
  So that I can complete my purchase

  Scenario: Login before checkout and place order
    Given I navigate to the home page
    When I click on Signup/Login link
    When I enter correct email and password
    And I click Login button
    Then I should be logged in as the user
    When I click Products link
    And I add first product to cart
    And I click View Cart
    And I click Proceed To Checkout
    Then I should see checkout page
    When I enter comment "Urgent delivery needed"
    And I click Place Order
    When I enter payment details
    And I click Pay and Confirm Order
    Then I should see order success message
    When I click Delete Account link
    Then I should see "ACCOUNT DELETED!" message