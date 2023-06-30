from class_data import ParsingAvito
import csv


def main():
    methods_parser = ParsingAvito(version_main=114, url='https://www.avito.ru/chita/kvartiry/sdam/posutochno'
                                                        '/-ASgBAgICAkSSA8gQ8AeSUg')
    prices = methods_parser.get_prices()
    titles = methods_parser.get_titles()
    methods_parser.out_driver()

    with open('result.csv', mode='w', encoding='utf-8') as file_w:
        file_writer = csv.writer(file_w, delimiter=';')
        file_writer.writerow(['Цена', 'Название'])
        for price, title in zip(prices, titles):
            file_writer.writerow([price, title])


if __name__ == '__main__':
    main()