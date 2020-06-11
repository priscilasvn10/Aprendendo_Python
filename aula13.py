lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]



except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por O')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando não ocorrer exceção')

finally:
    print('Sempre executar')
    print('Fechando o arquivo')
    arquivo.close()