import sys
from stores.elogroalegre import elogroalegre
from stores.invictvs import invictvs
from stores.lacuevadelokami import lacuevadelokami
from stores.losjuegosdeulthar import losjuegosdeulthar
from stores.ludisterra import ludisterra
from stores.mrdm import mrdm
from bcolors import bcolors

print

items = []
items.extend(elogroalegre.getItems(sys.argv[1]))
items.extend(invictvs.getItems(sys.argv[1]))
items.extend(lacuevadelokami.getItems(sys.argv[1]))
items.extend(losjuegosdeulthar.getItems(sys.argv[1]))
items.extend(ludisterra.getItems(sys.argv[1]))
items.extend(mrdm.getItems(sys.argv[1]))

print

for item in items:
    stock = ''
    if not item['stock']:
        stock = bcolors.FAIL + 'Sin stock' + bcolors.ENDC + ' | '
    print(bcolors.OKBLUE + item['store'] + bcolors.ENDC + ' | ' + bcolors.HEADER + item['title'].encode('utf-8') +
          bcolors.ENDC + ' | ' + bcolors.OKGREEN + item['price'] + bcolors.ENDC + ' | ' + stock + item['url'])
