import csv


class WriteFile:
    def __init__(self, prices, titles, links):
        self.prices = prices
        self.titles = titles
        self.links = links

    def write_csv(self):
        with open('result.csv', mode='w', encoding='utf-8') as file_w:
            file_writer = csv.writer(file_w, delimiter=';')
            file_writer.writerow(['Цена', 'Название', 'Ссылка'])
            for price, title, link in zip(self.prices, self.titles, self.links):
                file_writer.writerow([price, title, link])