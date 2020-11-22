# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from radish import given

from radish import world


@given("I start the chromium browser")
def nothing(step):
    desired = DesiredCapabilities.CHROME
    step.context.webdriver = webdriver.Chrome(
            desired_capabilities=desired,
            chrome_options=world.chrome_options())
    time.sleep(10)
