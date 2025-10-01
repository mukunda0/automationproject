Feature: Search Product
  As a user
  I want to search for products
  So that I can find specific items

  Scenario: Search for a product
    Given I navigate to the home page
    Then I should see the home page
    When I click Products link
    Then I should see all products page
    When I search for product "Tshirt"
    Then I should see SEARCHED PRODUCTS