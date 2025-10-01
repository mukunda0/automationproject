@api
Feature: API - POST To Verify Login with invalid details
  As an API user
  I should get error when logging in with invalid credentials

  Scenario: Login with invalid credentials via API
    When I send POST request to login with invalid credentials
    Then response code should be 404
    And response should indicate login failed