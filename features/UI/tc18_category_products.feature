Feature: View Category Products
  As a user
  I want to view products by category
  So that I can browse specific types of products

  Scenario: View products in Women Dress category
    Given I navigate to the home page
    When I click on Women category
    And I click on Dress subcategory
    Then I should see category page for Dress

  Scenario: Navigate between categories
    Given I navigate to the home page
    When I click on Women category
    And I click on Dress subcategory
    Then I should see category page for Dress
    When I click on Men category
    And I click on Tshirts subcategory
    Then I should see category page for Tshirts