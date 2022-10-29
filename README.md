# acre

A behavior driven dockerized system-level application test environment.

See https://github.com/realtimeprojects/acre-test for test examples.

Watch the [sample video](https://github.com/realtimeprojects/acre/wiki/navigation.feature.subtitles.mp4) of a automated test recording.

# features

- based on radish BDD
- run your BDD test in a docker container
- record videos from testruns
- create validation-ready test reports in zero time
- monitor live run with vnc or screen sharing

- supports selenium testing with chrome browser

## planned

- support ios and android platform testing (based on selenium)

# installation

## prerequisites

  - docker installed
  - linux or macos platform

## quickstart

  - install acre-cli

        pip3 install --upgrade https://github.com/realtimeprojects/acre-cli

  - clone acre-test project

        git clone https://github.com/realtimeprojects/acre-test

  - initialise acre

        acre init

  - run existing acre-tests

        cd acre-test
        acre features/*

