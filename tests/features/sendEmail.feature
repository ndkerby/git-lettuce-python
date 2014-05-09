Feature: Send email using SendGrid Mail API
 
Scenario: Test sending basic email
  Given I want to send an email
  I want to send an email to "ndkerby@gmail.com", from "ndkerby@gmail.com", with the subject "Testing 1 2 3" 
  Then I call the mail api
  I should recieve a success message
