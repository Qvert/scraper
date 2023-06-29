from selenium.webdriver.common.by import By


class ParsingAvito:
    def __init__(self, url, driver):
        self.get_page = driver.get(url)

