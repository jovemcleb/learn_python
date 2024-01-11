#Calculador de descontos
discount = float(input('Digite o valor do desconto: '))
converted_discount = discount / 100

product_value = float(input('Digite o valor do produto: '))
product_with_discount = product_value * (1 - converted_discount)

print('O valor do produto é R$ {:.2f}, como desconto fica R$ {:.2f}'.format(product_value, product_with_discount))
