Feature: Download Invoice after purchase confirmation
  As a user
  I want to download invoice after purchase
  So that I have proof of purchase

  Scenario: Place order and download invoice
    Given I navigate to the home page
    When I click Products link
    And I add first product to cart
    And I click View Cart
    And I click Proceed To Checkout
    And I click Register/Login from modal
    When I enter name and email for signup
    And I click Signup button
    When I fill account details
    And I fill address details
    And I click Create Account button
    When I click Continue button
    And I click Cart link
    And I click Proceed To Checkout
    When I enter comment "Invoice required"
    And I click Place Order
    When I enter payment details
    And I click Pay and Confirm Order
    Then I should see order success message
    When I click Download Invoice
    Then invoice should be downloaded
    When I click Continue button
    And I click Delete Account link
    Then I should see "ACCOUNT DELETED!" message