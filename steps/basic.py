# -*- coding: utf-8 -*-

from radish import given, when, then


@given("nothing")
def nothing(step):
    pass


@then("I expect nothing")
def i_expect_nothing(step):
    pass


@when("I say '{message}'")
def i_say(step, message):
    print("*** {}".format(message))
