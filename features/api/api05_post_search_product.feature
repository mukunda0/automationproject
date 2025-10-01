@api
Feature: API - POST To Search Product
  As an API user
  I want to search for products
  So that I can find specific items

  Scenario: Search product with valid search term
    When I send POST request to search product with name "Tshirt"
    Then response code should be 200
    And response should contain searched products