Feature: Register User with existing email
  As a user
  I should not be able to register with existing email
  So that email uniqueness is maintained

  Scenario: Attempt to register with existing email
    Given I navigate to the home page
    When I click on Signup/Login link
    Then I should see "New User Signup!" text
    When I enter name and email for signup
    And I click Signup button
    When I fill account details
    And I fill address details
    And I click Create Account button
    And I click Continue button
    And I click Logout link
    When I click on Signup/Login link
    When I enter name and email for signup
    And I click Signup button
    Then I should see signup error message