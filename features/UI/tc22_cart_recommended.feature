Feature: Add to cart from Recommended items
  As a user
  I want to add recommended products to cart
  So that I can purchase suggested items

  Scenario: Add recommended product to cart
    Given I navigate to the home page
    When I scroll to bottom of page
    Then I should see RECOMMENDED ITEMS
    When I add recommended product to cart
    And I click View Cart
    Then I should be on cart page