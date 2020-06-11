# for x in range(100): #imprime de 0 até 99
#     print(x)
#
# for x in range(90,101):
#     print('Novo: {}' .format(x))

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

# a = int (input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#      print(num)
# else:
#     print('Número {} não é primo'.format(a))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)