conjunto = {1,2,3,4}

conjunto2 = {1,2,3,4,5}
conjunto3 = {5,6,7,8}
conjunto_uniao = conjunto2.union(conjunto3)
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto2.intersection(conjunto3)
print('Intersecção : {}'.format(conjunto_interseccao))

conjunto_diferenca = conjunto2.difference(conjunto3)
print('diferença entre 2 e 3: {}'.format(conjunto_diferenca))

conjunto_diferenca2 = conjunto3.difference(conjunto2)
print('diferença entre 3 e 2: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto2.symmetric_difference(conjunto3)
print('Difereça com simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)#subconjunto
print('A é subconjunto de B {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A {}'.format(conjunto_superset))

lista_teste = ['cachorro','cachorro','gato','gato','elefante']
conjunto_animais= set(lista_teste) #tira a duplicidade e converte a conjunto
print(conjunto_animais)

list_animais = list(conjunto_animais)
print (conjunto_animais)


# print(type(conjunto))#conjunto é set
# print(conjunto)
#
# conjunto.add(5)
# print(conjunto)
#






