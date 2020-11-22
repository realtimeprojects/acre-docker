# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from radish import given, then, when

from radish import world


@given("I start the chromium browser")
def i_start_the_browser(step):
    desired = DesiredCapabilities.CHROME
    step.context.webdriver = webdriver.Chrome(
            desired_capabilities=desired,
            chrome_options=world.chrome_options())


@when("I navigate to '{url}'")
def i_navigate_to(step, url):
    print("opening url '{}'".format(url))
    step.context.webdriver.get(url)


@then("I see '{title}' in the page title")
def i_see_the_title(step, title):
    print("checking title %s" % title)
    world.asserts.contains(title, step.context.webdriver.title)
