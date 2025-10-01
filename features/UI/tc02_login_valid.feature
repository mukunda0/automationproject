Feature: User Login with Valid Credentials
  As a registered user
  I want to login with valid credentials
  So that I can access my account

  Scenario: Login with correct email and password
    Given I navigate to the home page
    Then I should see the home page
    When I click on Signup/Login link
    Then I should see "Login to your account" text
    When I enter correct email and password
    And I click Login button
    Then I should be logged in as the user
    When I click Delete Account link
    Then I should see "ACCOUNT DELETED!" message