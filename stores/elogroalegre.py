import requests
from lxml import html
from bcolors import bcolors


def has_stock(item):
    labels = item.xpath(
        './/div[@class="item-label-no-stock font-small-extra-xs"]')
    if len(labels) > 0:
        return False
    return True


class elogroalegre:
    @staticmethod
    def getItems(title):
        print('Buscando ' + bcolors.HEADER + title + bcolors.ENDC + ' en ' + bcolors.OKBLUE +
              'El Ogro Alegre' + bcolors.ENDC + '...'),

        url = 'https://www.elogroalegre.com.ar/search/?q=' + title

        response = requests.get(url)
        doc = html.fromstring(response.content)

        results = doc.xpath('//div[@class="item"]')

        items = []
        for i in range(len(results)):
            item = {
                'store': 'El Ogro Alegre',
                'title': results[i].xpath('.//a[@class="item-name product-item_name"]')[0].get('title'),
                'price': results[i].xpath('.//span[@class="price item-price p-left-quarter"]/text()')[0].strip(),
                'url': results[i].xpath('.//a[@class="item-name product-item_name"]')[0].get('href'),
                'stock': has_stock(results[i])
            }
            items.append(item)

        if len(items) != 1:
            print(str(len(items)) + ' items encontrados')
        else:
            print(str(len(items)) + ' item encontrado')

        return items
