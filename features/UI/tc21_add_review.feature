Feature: Add Review on Product
  As a user
  I want to add a review on a product
  So that I can share my opinion

  Scenario: Write and submit product review
    Given I navigate to the home page
    When I click Products link
    Then I should see all products page
    When I click on View Product of first product
    Then I should see product detail page
    When I write review with name "John Doe" email "john@test.com" and review "Great product!"
    Then I should see review success message