@tid:9002
Feature: Say hello world to the test run
    In order to monitor running tests
    I need to be able echo messages to the test run
    to test my software.

    Scenario: Say hello
        Given nothing
        When I say "Hello, World"
        Then I expect nothing
