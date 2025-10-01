Feature: Search Products and Verify Cart After Login
  As a user
  I want to search products and add to cart
  So that cart persists after login

  Scenario: Search product, add to cart, and verify after login
    Given I navigate to the home page
    When I click Products link
    Then I should see all products page
    When I search for product "Tshirt"
    Then I should see SEARCHED PRODUCTS
    When I add first product to cart
    And I click View Cart
    Then I should be on cart page
    When I click on Signup/Login link
    When I enter correct email and password
    And I click Login button
    And I click Cart link
    Then I should be on cart page