@api
Feature: API - Get All Brands List
  As an API user
  I want to get all brands
  So that I can display them

  Scenario: Get all brands list via API
    When I send GET request to brands list
    Then response code should be 200
    And response should contain brands list