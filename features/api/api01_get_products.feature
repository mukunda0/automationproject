@api
Feature: API - Get All Products List
  As an API user
  I want to get all products
  So that I can display them

  Scenario: Get all products list via API
    When I send GET request to products list
    Then response code should be 200
    And response should contain products list