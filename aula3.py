# Continuação dos 100 excercicios 
#  15 ao 40

# if else == elif

# print("Exercicio 16")
# print("-" * 15)
# num = int(input("Digite um numero: "))
# if num < 0 :
#     print("Negativo")
# else:
#     print("Positivo")

# print("-" * 15)

# print("Exercicio 17")
# print("-" * 15)

# a = int(input("Digite um numero: "))

# if a % 2 == 0:
#     print("Par")
# else :
#     print("Impar")

# print("-" * 15)

# print("Exercicio 18")
# print("-" * 15)

# primeiroValor = int(input("Digite o primeiro numero: "))
# segundoValor = int(input("Digite o segundo valor: "))
# if primeiroValor > segundoValor:
#     print(f"Maior valor : {primeiroValor}")
# elif segundoValor > primeiroValor:
#     print(f"Maior valor : {segundoValor}")
# else :
#     print("Valores iguais")
    
print("-" * 15)

print("Exercicio 19")
print("-" * 15)

# primeiro = int(input("Digite o primeiro valor: "))
# segundo = int(input("Digite o segundo valor: "))
# terceiro = int(input("Digite o terceiro valor: "))

# if primeiro < segundo > terceiro:
#     print(f"Maior numero : {segundo}")
# elif segundo < primeiro > terceiro:
#     print(f"maior numero : {primeiro}")
# else :
#     print(f"maior numero: {terceiro}")

# if primeiro > segundo < terceiro :
#     print(f"menor numero: {segundo}")
# elif segundo > primeiro < terceiro:
#     print(f"menor numero: {primeiro}")
# else:
#     print(f"menor numero : {terceiro}")
    
print("-" * 15)

print("Exercicio 20")
print("-" * 15)

# pi = int(input("digite o primeiro numero: "))
# se = int(input("digite o segundo numero: "))
# te = int(input("digite o terceiro numero: "))

# if pi >= se and pi >= te:
#     if se >= te :
#         print(f"ordem crescente: {te, se, pi}")
#     else :
#         print(f"ordem crescente: {se, te, pi}")
# elif se >= pi and se >= te :
#     if te >= pi:
#         print(f"ordem crescente: {pi, te, se}")
#     else :
#         print(f"ordem crescente: {te, pi, se}")
# elif te >= pi and te >= se:
#     if pi >= se :
#         print(f"ordem crescente: {se, pi, te}")
#     else :
#         print(f"ordem crescente: {pi, se , te}")

print("-" * 15)

print("Exercicio 21")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = nota1 + nota2 // 2
if media >= 7:
    print(f"{media}: Aprovado")
else:
    print(f"{media}: Reprovado")
print("-" * 15)

print("Exercicio 22")

notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))
mediaNota = notaA + notaB / 2
if mediaNota <5:
    print(f"{mediaNota}: Reprovado")
elif mediaNota >= 5 and mediaNota <7:
    print(f"{mediaNota}: Recuperacao")
else:
    print(f"{mediaNota}: Aprovado")

print("-" * 15)
print("Exercicio 23")

voto_Idade = int(input("Digite sua idade: "))

if voto_Idade < 16:
    print("Não pode votar")
elif voto_Idade == 16 or voto_Idade ==17:
    print("Voto opcional")
elif voto_Idade >=18 and voto_Idade <= 69:
    print("Voto obrigatorio")
else:
    print("Voto opcional")

print("*" * 15)
print("Exercicio 24")

ano = int(input("Digite um ano: "))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print("Ano bissexto")
else:
        print("Nao e ano bissexto")

print("*" * 15)
print("Exercicio 25")

precoConta = float(input("Digite um preco: "))
print("""
1 - Dinheiro ou Pix
2 - Débito 
3 - Crédito à vista 
4 - Crédito parcelado
""")
opcaoConta = int(input("Digite uma opção: "))
desconto = 0
total = 0
if opcaoConta == 1 :
     desconto = precoConta * 0.10
     total = precoConta - desconto
     print(f"Total da compra: {total}")
elif opcaoConta == 2 :
     desconto = precoConta * 0.05
     total = precoConta - desconto
     print(f"Total da compra: {total}")
elif opcaoConta == 3 :
      print(f"Total da compra: {precoConta}")
elif opcaoConta == 4 :
     desconto = precoConta * 0.08
     total = precoConta + desconto
     print(f"Total da compra: {total}")

print("*" * 15)
print("Exercicio 26")

atual_Salario = float(input("Digite o salario atual: "))
percentual = int(input("informe o percentual de ajuste: "))
rejuste = atual_Salario * percentual/100
total = atual_Salario + rejuste

print(f"salario atual: {atual_Salario}; percentual : {percentual}; valor do aumento: {rejuste}")
print(f"Novo salario: {total}")


print("*" * 15)
print("Exercicio 27")

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
     print(imc)
     print("Abaixo da faixa")
elif imc >= 18.5 and imc < 25:
     print(imc)
     print("Faixa normal")
elif imc >= 25 and imc < 30:
     print(imc)
     print("Acima da faixa")
else :
     print(imc)
     print("Faixa Elevada")


print("*" * 15)
print("Exercicio 28")

medidaA = int(input("Digite uma medida: "))
medidaB = int(input("Digite uma medida: "))
medidaC = int(input("Digite uma medida: "))
# if medidaA < medidaB + medidaC and medidaA < medidaC + medidaB:
#      print("Forma triangulo")
# elif medidaB < medidaA + medidaC and medidaB < medidaC + medidaA:
#      print("Formam um triangulo")
# elif medidaC < medidaA + medidaB and medidaC < medidaB + medidaA:
#      print("Formam triangulo")
# else:
#      print("Não formam um triangulo")
if medidaA < medidaB + medidaC and medidaB < medidaC + medidaA and medidaC < medidaA + medidaB:
          print("Formam triangulo")
else:
     print("Nao formam triangulo")
     
print("*" * 15)
print("Exercicio 29")