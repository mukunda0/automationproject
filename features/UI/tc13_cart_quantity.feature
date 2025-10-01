Feature: Verify Product Quantity in Cart
  As a user
  I want to increase product quantity
  So that I can buy multiple units

  Scenario: Verify product quantity can be increased
    Given I navigate to the home page
    Then I should see the home page
    When I click Products link
    And I click on View Product of first product
    When I increase quantity to 4
    And I click Add to cart button
    And I click View Cart
    Then I should be on cart page
    And product quantity should be 4