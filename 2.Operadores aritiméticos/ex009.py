# tabuada de um número

cont = 1
num = int(input('Digite um número: '))

for i in range(10):
    print('{} x {} = {}'.format(num, cont, num * cont))
    cont += 1
