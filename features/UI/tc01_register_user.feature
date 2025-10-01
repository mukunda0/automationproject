Feature: User Registration
  As a new user
  I want to register on the website
  So that I can access member features

  Scenario: Register a new user successfully
    Given I navigate to the home page
    Then I should see the home page
    When I click on Signup/Login link
    Then I should see "New User Signup!" text
    When I enter name and email for signup
    And I click Signup button
    Then I should see "ENTER ACCOUNT INFORMATION" text
    When I fill account details
    And I fill address details
    And I click Create Account button
    Then I should see "ACCOUNT CREATED!" message
    When I click Continue button
    Then I should be logged in as the user
    When I click Delete Account link
    Then I should see "ACCOUNT DELETED!" message
    And I click Continue button