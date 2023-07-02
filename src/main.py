from class_data import ParsingAvito


def main():
    methods_parser = ParsingAvito(version_main=114, url='https://www.avito.ru/chita/kvartiry/sdam/posutochno'
                                                        '/-ASgBAgICAkSSA8gQ8AeSUg')
    prices = methods_parser.get_prices()
    titles = methods_parser.get_titles()
    links = methods_parser.get_links()
    methods_parser.out_driver()


if __name__ == '__main__':
    main()