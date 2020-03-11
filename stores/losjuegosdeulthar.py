import requests
from lxml import html
from bcolors import bcolors


def has_stock(item):
    labels = item.xpath(
        './/div[@class="labels"]/div[@class="label label-default"]/text()')
    if len(labels) > 0:
        if labels[0].strip() == 'Sin stock':
            return False
    return True


class losjuegosdeulthar:
    @staticmethod
    def getItems(title):
        print('Buscando resultados en ' + bcolors.OKBLUE +
              'Los juegos de Ulthar' + bcolors.ENDC + '...'),

        url = 'https://www.losjuegosdeulthar.com.ar/search/?q=' + title

        response = requests.get(url)
        doc = html.fromstring(response.content)

        results = doc.xpath('//div[@class="col-6 col-md-3 item item-product"]')

        items = []
        for i in range(len(results)):
            item = {
                'store': 'Los juegos de Ulthar',
                'title': results[i].xpath('.//a[@class="js-item-link item-link position-absolute w-100"]')[0].get('title'),
                'price': results[i].xpath('.//span[@class="js-price-display item-price"]/text()')[0].strip(),
                'url': results[i].xpath('.//a[@class="js-item-link item-link position-absolute w-100"]')[0].get('href'),
                'stock': has_stock(results[i])
            }
            items.append(item)

        if len(items) != 1:
            print(str(len(items)) + ' items encontrados')
        else:
            print(str(len(items)) + ' item encontrado')

        return items
