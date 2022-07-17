# 40688134000161
# 04252011000110
def converter(cnpj, lista):
    for c in cnpj:
        c = int(c)
        lista.append(c)


def lista_multiplicadora(lista_novo, lista_formula, lista_multiplica):
    for i in range(len(lista_novo)):
        resultado = lista_novo[i] * lista_formula[0]
        lista_multiplica.append(resultado)
        lista_formula.pop(0)


def somar_lista(lista):
    soma = 0
    for c in range(len(lista)):
        soma += lista[c]
    return soma


def string(lista, cnpj):
    for c in lista:
        c = str(c)
        cnpj += c
    return cnpj


cnpj = input('CNPJ: ')
novo_cnpj = cnpj[:-2]
lista_formula = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista_formula2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista_novo_cnpj = list()
lista_multiplicar = list()
cnpj_final = ''

converter(novo_cnpj, lista_novo_cnpj)
lista_multiplicadora(lista_novo_cnpj, lista_formula, lista_multiplicar)

primeiro_digito = 11 - (somar_lista(lista_multiplicar) % 11)
if primeiro_digito > 9:
    primeiro_digito = 0

lista_novo_cnpj.append(primeiro_digito)
lista_multiplicar = []
lista_multiplicadora(lista_novo_cnpj, lista_formula2, lista_multiplicar)

segundo_digito = 11 - (somar_lista(lista_multiplicar) % 11)
if segundo_digito > 9:
    segundo_digito = 0

lista_novo_cnpj.append(segundo_digito)
calculo_final = string(lista_novo_cnpj, cnpj_final)

if calculo_final == cnpj:
    print(f'A CNPJ: {cnpj} é válida!')
else:
    print(f'A CNPJ: {cnpj} é invalida!')
