Feature: User Login with Invalid Credentials
  As a user
  I want to see an error message
  When I try to login with invalid credentials

  Scenario: Login with incorrect email and password
    Given I navigate to the home page
    Then I should see the home page
    When I click on Signup/Login link
    Then I should see "Login to your account" text
    When I enter incorrect email and password
    And I click Login button
    Then I should see login error message "Your email or password is incorrect!"