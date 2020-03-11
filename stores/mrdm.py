import requests
from lxml import html
from bcolors import bcolors


def has_stock(item):
    for classname in item.classes:
        if classname == 'outofstock':
            return False
    return True


class mrdm:
    @staticmethod
    def getItems(title):
        print('Buscando resultados en ' + bcolors.OKBLUE +
              'Mr DM' + bcolors.ENDC + '...'),

        url = 'https://mrdm.store/?post_type=product&s=' + title

        response = requests.get(url)
        doc = html.fromstring(response.content)

        results = doc.xpath(
            '//li[contains(@class, "product type-product")]')

        items = []
        for i in range(len(results)):
            item = {
                'store': 'Mr DM',
                'title': results[i].xpath('.//h2[@class="woocommerce-loop-product_title"]/a/text()')[0],
                'price': results[i].xpath('.//span[@class="price"]/span[@class="woocommerce-Price-amount amount"]/text()')[0].strip(),
                'url': results[i].xpath('.//h2[@class="woocommerce-loop-product_title"]/a')[0].get('href'),
                'stock': has_stock(results[i])
            }
            items.append(item)

        if len(items) != 1:
            print(str(len(items)) + ' items encontrados')
        else:
            print(str(len(items)) + ' item encontrado')

        return items
