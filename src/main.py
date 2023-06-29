from src.class_data import ParsingAvito


def main():
    methods_parser = ParsingAvito(version_main=114, url='https://www.avito.ru/chita/kvartiry/sdam/posutochno'
                                                        '/-ASgBAgICAkSSA8gQ8AeSUg')
    print(methods_parser.get_prices())


if __name__ == '__main__':
    main()