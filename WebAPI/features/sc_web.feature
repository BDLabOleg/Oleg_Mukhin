Feature: Response status code control
Scenario: Make request and check the status code of it
  Given a Site
  When the request is run
  Then the Site returns status code of request