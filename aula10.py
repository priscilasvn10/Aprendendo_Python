import shutil

arquivo = open('teste.txt', 'w')
arquivo.write('Minha primeira escrita')
arquivo.close()
arquivo = open('teste.txt', 'a')
arquivo.write('\nSegunda escrita')
arquivo.close()


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def aulaizar_arquivo(nome_arquivo, texto):
    arquivo = open('texto.txt', 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)

    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        print(lista_notas)
        notas = lista_notas.pop(0)
        print(aluno)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C/Users/Gemeas/Desktop/Estudando_Python/')


# def move_arquivo:
#     import shutil
#     shutil.move(nome_arquivo, 'C/Users/Gemeas/Desktop/Estudando_Python/')


if __name__ == '__main__':
    escrever_arquivo('linha teste.\n')
aluno = 'Cesar, 7,8,9,10\n'
#	atualizar_arquivo('notas.txt',aluno)
#	copia_arquivo('notas.txt')
#	move_arquivo('notas.txt')