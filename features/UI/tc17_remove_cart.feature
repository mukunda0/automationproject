Feature: Remove Products from Cart
  As a user
  I want to remove products from cart
  So that I can manage my shopping cart

  Scenario: Remove product from cart
    Given I navigate to the home page
    When I click Products link
    And I add first product to cart
    And I click View Cart
    Then I should be on cart page
    When I click X button to remove product
    Then product should be removed from cart