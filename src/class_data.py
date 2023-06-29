from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


class ParsingAvito:
    def __init__(self, url, version_main=None):
        self.url = url
        self.version_main = version_main
        self.option = uc.ChromeOptions()
        self.option.add_argument('--headless')
        self.driver = uc.Chrome(version_main=self.version_main, options=self.option)
        self.driver.get(self.url)

    def get_prices(self):
        prices = self.driver.find_elements(By.CLASS_NAME, 'price-price-JP7qe')
        list_prices = [i.text for i in prices]
        self.driver.close()
        self.driver.quit()
        return list_prices
