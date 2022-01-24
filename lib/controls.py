from selenium.webdriver.common.by import By

from radish import world


class Control():
    def __init__(self, tag="*", id=None, cssclass=None, text=None):
        filter = []
        filterstr = ""

        if id:
            filter.append(f"contains(@id, '{id}')")
        if cssclass:
            filter.append(f"contains(@class, '{cssclass}')")
        if text:
            filter.append(f"contains(text(), '{text}')")
        if len(filter) > 0:
            filterstr = f'[{" and ".join(filter)}]'
        self.xpath = f"//{tag}{filterstr}"

    def input(self, text):
        self.locate()
        self.match.send_keys(text)

    def locate(self):
        self.match = world.webdriver.find_element(By.XPATH, self.xpath)

    def click(self):
        self.locate()
        self.match.click()


class Input(Control):
    def __init__(self, id=None, cssclass=None, text=None):
        super().__init__(tag='input', id=id, cssclass=cssclass, text=text)


class Link(Control):
    def __init__(self, id=None, cssclass=None, text=None):
        super().__init__(tag='a', id=id, cssclass=cssclass, text=text)
