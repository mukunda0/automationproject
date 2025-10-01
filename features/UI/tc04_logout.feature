Feature: User Logout
  As a logged in user
  I want to logout
  So that I can secure my account

  Scenario: Logout user
    Given I navigate to the home page
    Then I should see the home page
    When I click on Signup/Login link
    When I enter correct email and password
    And I click Login button
    Then I should be logged in as the user
    When I click Logout link
    Then I should see "Login to your account" text