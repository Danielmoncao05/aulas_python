# Introdução de funções em linguagem pyhton

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

soma = soma(5,5)
print(soma)




# exercicios

# Exercício 1: Validação de Strings e Parâmetros

# Objetivo: Criar uma função que valide o tamanho de uma string, simulando uma
# consistência de dados.

# def leituraStrin (string):
#     resultado = len(string)
#     if resultado >= 1 and resultado <= 100 :
#          return True
#     else :
#         return False

# texto = str(input("digite um texto: "))
# print(leituraStrin(texto))

# Exercício 2: Cálculo de Imposto (Funções com Retorno)

# Objetivo: Praticar funções que realizam cálculos matemáticos e retornam
# resultados para o programa principal.

def soma_imposto(taxa_imposto, custo):
    desconto = taxa_imposto / 100
    custo_total = custo + desconto
    return custo_total

custo = float(input("digite o custo do produto : "))
taxa = int(input("digite a taxa de desconto : "))
print(soma_imposto(taxa, custo))