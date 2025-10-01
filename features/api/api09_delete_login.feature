@api
Feature: API - DELETE METHOD To Verify Login
  As an API user
  I should get error when using wrong HTTP method

  Scenario: DELETE to login endpoint should fail
    When I send DELETE request to login
    Then response code should be 405
    And response should contain error message