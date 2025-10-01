@api
Feature: API - PUT METHOD To Update User Account
  As an API user
  I want to update user account details
  So that I can modify user information

  Scenario: Update user account via API
    Given I have a timestamp
    When I send POST request to create account
    Then response code should be 201
    When I send PUT request to update account
    Then response code should be 200
    And response should indicate account updated