cost = int(input('Enter a value:'))
sell = int(input('Enter value:'))
if sell == cost:
    print('No profit no loss')
elif sell > cost:
    c = ((sell-cost)/cost)*100
    print('Profit is', c, '%')
else:
    d = ((cost-sell)/cost)*100
    print('Loss is', d, '%')
