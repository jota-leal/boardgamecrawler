import requests
from lxml import html
from bcolors import bcolors


def has_stock(item):
    labels = item.xpath(
        './/div[@class="product-grid-labels"]/div[@class="item-label product-label label-light font-small"]/text()')
    if len(labels) > 0:
        if labels[0].strip() == 'Sin stock':
            return False
    return True


class lacuevadelokami:
    @staticmethod
    def getItems(title):
        print('Buscando resultados en ' + bcolors.OKBLUE +
              'La cueva del Okami' + bcolors.ENDC + '...'),

        url = 'https://www.lacuevadelokami.com.ar/search/?q=' + title

        response = requests.get(url)
        doc = html.fromstring(response.content)

        results = doc.xpath(
            '//div[@class="span3 item-container m-bottom-half"]')

        items = []
        for i in range(len(results)):
            item = {
                'store': 'La cueva del Okami',
                'title': results[i].xpath('.//a[@class="item-name"]')[0].get('title'),
                'price': results[i].xpath('.//span[@class="item-price h6"]/text()')[0].strip(),
                'url': results[i].xpath('.//a[@class="item-name"]')[0].get('href'),
                'stock': has_stock(results[i])
            }
            items.append(item)

        if len(items) != 1:
            print(str(len(items)) + ' items encontrados')
        else:
            print(str(len(items)) + ' item encontrado')

        return items
