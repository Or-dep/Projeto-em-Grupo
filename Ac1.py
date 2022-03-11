# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 8 alunos)
# ALUNO 1: Kaua Coelho Santos                       RA: 2101877
# ALUNO 2: Murillo Casemiro Leta                    RA: 2101980
# ALUNO 3: Pedro Henrique do Carmo Alencar          RA: 2102268
# ALUNO 4: Rafael Vicente Benito da Costa Rodrigues RA: 2102496
# ALUNO 5: Wellington Rodrigues da Silva            RA: 2102474


'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e dois itens e retorna True, se os dois itens estiverem
armazenado na lista, e False, caso contrário.
'''


def pertence(lista, item1, item2): # ok #pedro
    ct = 0
    for valor in lista:
        if valor == item1 or valor == item2:
            ct += 1
        else:
            pass
    if ct == 2:
        resultado = True
    else:
        resultado = False
    return resultado


'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma lista e dois itens (velho e novo) e retorna uma lista onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo): #1 #kaua
    pass


'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item): #2 #rafa
    pass


'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
'''


def reprovados(alunos): #3 #well
    pass


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações
'''


def excluir_nota(alunos, nome): #4 #murilo
    pass


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maior_nota que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a maior nota
de cada aluno.
'''


def maior_nota(alunos): #5 #pedro
    pass