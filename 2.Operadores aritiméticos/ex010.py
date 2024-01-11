# Conversor de real para dolar

DOLAR_VALUE = 4.87

wallet = float(input('Informe o valor que você quer converter para dolar: '))

converted_value = wallet / DOLAR_VALUE

print('{} reais equivale a {:.2f} dólares'.format(wallet, converted_value))
