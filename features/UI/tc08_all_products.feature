Feature: Verify All Products and Product Detail Page
  As a user
  I want to view all products
  So that I can browse available items

  Scenario: View all products and product details
    Given I navigate to the home page
    Then I should see the home page
    When I click Products link
    Then I should see all products page
    And products list should be visible
    When I click on View Product of first product
    Then I should see product detail page