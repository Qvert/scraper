import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
options.add_argument("--headless")
driver = uc.Chrome(version_main=114, options=options)

try:
    driver.get('https://www.avito.ru/chita?q=геймпад')
    push = driver.find_elements(By.CLASS_NAME, 'styles-module-root-LIAav')
    for elem in push:
        print(elem.text)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


def main():
    pass


if __name__ == '__main__':
    main()