Feature: Add Products to Cart
  As a user
  I want to add multiple products to cart
  So that I can purchase them together

  Scenario: Add multiple products to cart
    Given I navigate to the home page
    Then I should see the home page
    When I click Products link
    When I add first product to cart
    And I click Continue Shopping
    When I add second product to cart
    And I click View Cart
    Then I should be on cart page
    And both products should be in cart