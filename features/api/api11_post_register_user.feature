@api
Feature: API - POST To Create/Register User Account
  As an API user
  I want to create a new account
  So that I can register on the platform

  Scenario: Create new user account via API
    Given I have a timestamp
    When I send POST request to create account
    Then response code should be 201
    And response should indicate account created
    When I send DELETE request to delete account
    Then response code should be 200
    And response should indicate account deleted