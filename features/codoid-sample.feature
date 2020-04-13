@launch.browser
Feature: Codoid Website Feature

Scenario: Contact Codoid Team
  Given I am on home page
  When I submit contact us form
  Then I should see Thank You page with a message