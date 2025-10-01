@api
Feature: API - POST To Verify Login without email parameter
  As an API user
  I should get error when email parameter is missing

  Scenario: Login without email parameter
    When I send POST request to login without email
    Then response code should be 400
    And response should indicate missing parameter