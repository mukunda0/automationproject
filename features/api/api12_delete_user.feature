@api
Feature: API - DELETE METHOD To Delete User Account
  As an API user
  I want to delete user account
  So that I can remove users from the system

  Scenario: Delete user account via API
    Given I have a timestamp
    When I send POST request to create account
    Then response code should be 201
    When I send DELETE request to delete account
    Then response code should be 200
    And response should indicate account deleted