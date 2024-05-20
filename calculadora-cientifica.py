import math

print('Olá! Digite os números a seguir para fazer os cálculos: (1)adição, (2)subtração, (3)multplicação, (4)divisão (5)raiz quadrada')

p1 = int(input('Qual cálculo fazer?: '))

if p1 == 1:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(n1 + n2)

if p1 == 2:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(n1 - n2)

if p1 == 3:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(n1 * n2)

if p1 == 4:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(n1 / n2)

if p1 == 5:
    n1 = int(input('Digite o primeiro número: '))
    print(math.sqrt(n1))

