# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

sales = OrderedDict()

num = int(input())

for _ in range(num):
    entries = input().split()
    item_name = []
    for entry in entries:
        try:
            net_price = int(entry)
        except ValueError:
            item_name.append(entry)
    item_name = ' '.join(item_name)
    
    if item_name in sales:
        sales[item_name] += int(net_price)
    else:
        sales[item_name] = net_price

for item, price in sales.items():
    print(item, price)
