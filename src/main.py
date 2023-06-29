import undetected_chromedriver as uc
from src.class_data import ParsingAvito


def main():
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(version_main=114, options=options)
    methods_parser = ParsingAvito(url='https://www.avito.ru/chita?q=геймпад', driver=driver)


if __name__ == '__main__':
    main()