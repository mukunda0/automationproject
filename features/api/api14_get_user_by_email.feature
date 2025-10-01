@api
Feature: API - GET user account detail by email
  As an API user
  I want to get user details by email
  So that I can retrieve user information

  Scenario: Get user details by email via API
    Given I have a timestamp
    When I send POST request to create account
    Then response code should be 201
    When I send GET request to get user by email
    Then response code should be 200
    And response should contain user details