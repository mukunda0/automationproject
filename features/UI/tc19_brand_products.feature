Feature: View Brand Products
  As a user
  I want to view products by brand
  So that I can see all items from my favorite brands

  Scenario: View products from Polo brand
    Given I navigate to the home page
    When I click Products link
    Then I should see brands in sidebar
    When I click on Polo brand
    Then I should see brand page for Polo

  Scenario: Navigate between brands
    Given I navigate to the home page
    When I click Products link
    When I click on Polo brand
    Then I should see brand page for Polo
    When I click on H&M brand
    Then I should see brand page for H&M