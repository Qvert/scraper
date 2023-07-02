from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


class ParsingAvito:
    def __init__(self, url: str, version_main=None):
        self.url = url
        self.version_main = version_main
        self.option = uc.ChromeOptions()
        self.option.add_argument('--headless')
        self.driver = uc.Chrome(version_main=self.version_main, options=self.option)
        self.driver.get(self.url)

    def get_prices(self) -> list:
        prices = self.driver.find_elements(By.CLASS_NAME, 'price-price-JP7qe')
        list_prices = [i.text for i in prices]
        return list_prices

    def get_titles(self) -> list:
        titles = self.driver.find_elements(By.CLASS_NAME, 'iva-item-title-py3i_')
        list_titles = [i.text for i in titles]
        return list_titles

    def get_links(self) -> list:
        links = self.driver.find_elements(By.CLASS_NAME, 'iva-item-title-py3i_')
        list_links = [i.find_element(By.TAG_NAME, 'a').get_attribute('href') for i in links]
        return list_links

    def out_driver(self) -> None:
        self.driver.close()
        self.driver.quit()