# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from radish import given, then, when, step

from radish import world


@given("I start the chromium browser")
def i_start_the_browser(step):
    desired = DesiredCapabilities.CHROME
    world.webdriver = webdriver.Chrome(
            desired_capabilities=desired,
            options=world.chrome_options())


@step("I close the browser")
def i_close_the_browser(step):
    world.webdriver.close()


@when("I navigate to '{url}'")
def i_navigate_to(step, url):
    print(f"opening url '{url}'")
    world.webdriver.get(url)


@then("I see '{title}' in the page title")
def i_see_the_title(step, title):
    print(f"checking title {title}")
    world.asserts.contains(title, world.webdriver.title)
