@api
Feature: API - POST To Verify Login with valid details
  As an API user
  I want to login with valid credentials
  So that I can access my account

  Scenario: Login with valid credentials via API
    When I send POST request to login with email "testuser@test.com" and password "test123"
    Then response code should be 200