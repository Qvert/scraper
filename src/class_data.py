from selenium.webdriver.common.by import By


class ParsingAvito:
    def __init__(self, url, driver):
        self.get_page = driver.get(url)

    def get_prices(self):
        prices = self.get_page.find_elements(By.CLASS_NAME, 'price-price-JP7qe')
        list_prices = [i.text for i in prices]
        return list_prices