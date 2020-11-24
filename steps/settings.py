from radish import pick

from selenium import webdriver


@pick
def chrome_options():
    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1024,800")
    return chrome_options
