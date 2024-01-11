# Latas de tinta necessárias para pintar uma parede

LITRO_DE_TINTA = 2.0

height = float(input('Digite a altura da parede'))
width = float(input('Digite a largura da parede'))

area = width * height
litros_necessarios = area / LITRO_DE_TINTA

print('Será necessário {:.2f} litros de tinta para pintar {}m²'.format(litros_necessarios, area))
