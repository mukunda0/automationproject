@api
Feature: API - POST To All Products List
  As an API user
  I should get error when using wrong HTTP method

  Scenario: POST to products list should fail
    When I send POST request to products list
    Then response code should be 405
    And response should contain error message