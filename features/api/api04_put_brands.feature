@api
Feature: API - PUT To All Brands List
  As an API user
  I should get error when using wrong HTTP method

  Scenario: PUT to brands list should fail
    When I send PUT request to brands list
    Then response code should be 405
    And response should contain error message