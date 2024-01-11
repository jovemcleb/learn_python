#Calculador de acréscimos

addition = float(input('Digite o valor do acréscimo: '))
converted_addition = addition / 100

wage = float(input('Digite o valor do salário: '))
wage_with_addition = wage * (1 + converted_addition)

print('O salário era de R${:.2f}, com o acréscimo ficou R${:.2f}'.format(wage, wage_with_addition))

