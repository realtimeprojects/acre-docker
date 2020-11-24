@tid:9002
@regression
Feature: start a browser
    In order to test web applications
    I need to be able to start the browser from the test.

    Scenario: open github.com
        Given I start the chromium browser
        When I navigate to 'http://www.github.com'
        Then I see 'GitHub' in the page title

    Scenario: open radish on github.com
        Given I start the chromium browser
        When I navigate to 'https://github.com/radish-bdd/radish'
        Then I see 'radish-bdd' in the page title
