from class_data import ParsingAvito
from class_write_to_file import WriteFile


def main():
    methods_parser = ParsingAvito(version_main=114, url='https://www.avito.ru/chita/kvartiry/sdam/posutochno'
                                                        '/-ASgBAgICAkSSA8gQ8AeSUg')
    prices = methods_parser.get_prices()
    titles = methods_parser.get_titles()
    links = methods_parser.get_links()
    methods_parser.out_driver()

    file_result = WriteFile(prices, titles, links)
    file_result.write_csv()


if __name__ == '__main__':
    main()