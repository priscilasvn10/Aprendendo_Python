a= int(input('Entre com o primeiro valor: '))
b= int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print('soma: {}'.format(soma))
# print('subtração: {}'.format(subtracao))
# print('multiplicacao: {}' .format(multiplicacao))
# print('divisao: {}' .format(divisao))
#print('resto: {}' .format (resto))
resultado=('Soma: {som}'
           ' \nSubtração: {sub} '
      '\nMultiplicação: {mult}'
      '\n Divisão: {div}'
      '\n Resto: {res} '.format(som=soma, sub=subtracao, mult= multiplicacao, div=divisao, res=resto))
print(resultado)

