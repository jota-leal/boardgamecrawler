import requests
from lxml import html
from bcolors import bcolors


def has_stock(item):
    labels = item.xpath('.//span[@class="out-of-stock"]')
    if len(labels) > 0:
        return False
    return True


class invictvs:
    @staticmethod
    def getItems(title):
        print('Buscando resultados en ' + bcolors.OKBLUE +
              'Invictvs' + bcolors.ENDC + '...'),

        url = 'https://invictvs.com.ar/tienda/search?controller=search&orderby=position&orderway=desc&search_query_cat=0&search_query=' + title

        response = requests.get(url)
        doc = html.fromstring(response.content)

        results = doc.xpath(
            '//ul[@class="product_list grid row"]/li/div[@class="product-container"]')

        items = []
        for i in range(len(results)):
            item = {
                'store': 'Invictvs',
                'title': results[i].xpath('.//a[@class="product-name"]')[0].get('title'),
                'price': results[i].xpath('.//span[@class="price product-price"]/text()')[0].strip(),
                'url': results[i].xpath('.//a[@class="product-name"]')[0].get('href'),
                'stock': has_stock(results[i])
            }
            items.append(item)

        if len(items) != 1:
            print(str(len(items)) + ' items encontrados')
        else:
            print(str(len(items)) + ' item encontrado')

        return items
