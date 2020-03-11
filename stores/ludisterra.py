import requests
from lxml import html
from bcolors import bcolors


def has_stock(item):
    labels = item.xpath('.//span[@class="out-of-stock product-label"]')
    if len(labels) > 0:
        return False
    return True


class ludisterra:
    @staticmethod
    def getItems(title):
        print('Buscando resultados en ' + bcolors.OKBLUE +
              'Ludisterra' + bcolors.ENDC + '...'),

        url = 'https://ludisterra.com.ar/?post_type=product&s=' + title

        response = requests.get(url)
        doc = html.fromstring(response.content)

        results = doc.xpath(
            '//div[contains(@class, "product-grid-item product")]')

        items = []
        for i in range(len(results)):
            item = {
                'store': 'Ludisterra',
                'title': results[i].xpath('.//h3[@class="product-title"]/a/text()')[0],
                'price': results[i].xpath('.//span[@class="price"]/span[@class="woocommerce-Price-amount amount"]/text()')[0].strip(),
                'url': results[i].xpath('.//h3[@class="product-title"]/a')[0].get('href'),
                'stock': has_stock(results[i])
            }
            items.append(item)

        if len(items) != 1:
            print(str(len(items)) + ' items encontrados')
        else:
            print(str(len(items)) + ' item encontrado')

        return items
