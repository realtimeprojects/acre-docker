# acre

A behavior driven dockerized system-level application test environment.

See https://github.com/realtimeprojects/acre-test for test examples.

# features

- based on radish BDD
- run your BDD test in a docker container
- record videos from testruns
- create validation-ready test reports in zero time

- supports selenium testing with chrome browser

## planned

- support ios and android platform testing (based on selenium)

# installation

## prerequisites

  - gnu make installed
  - docker installed
  - linux or macos plattform

## quickstart

  - clone me from github:

        git clone https://github.com/realtimeprojects/acre

  - clone acre-test project

        git clone https://github.com/realtimeprojects/acre-test

  - install acre:

        acre/bin/install

  - run existing acre-tests

        cd acre-test
        acre

