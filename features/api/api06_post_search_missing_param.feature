@api
Feature: API - POST To Search Product without search_product parameter
  As an API user
  I should get error when search parameter is missing

  Scenario: Search product without parameter
    When I send POST request to search product without parameter
    Then response code should be 400
    And response should indicate missing parameter