#1) O Python trabalha tipos de valores. Com os valores abaixo, dê o nome dos seus tipos:

#a. 1 = inteiro

n1 = 1
print(type(n1))

#b. 12.6 = float
n2 = 12.6
print(type(n2))

# c. True = boleano
n3 = True
print(type(n3))

# d. False = boleaon
n4 = False
print(type(n4))

# e. -543 = inteiro
n5 = -543
print(type(n5))

# f. -5.78 = float
n6 = -5.70
print(type(n6))

# g. "copo" = string
n7 = "copo"
print(type(n7))

# h. 'belo dia' = string
n8 = 'belo dia'
print(type(n8))

# 2. Digite cada linha abaixo no Shell do Python e informe quais estão corretos e quais apresentam erro.
# 1
# Retorna 1

# 1a
# Dá erro

# a1 
# Dá erro

# 1.
# Retorna 1.0

# .2
# Retorna 0.2

# -.3
# Retorna -0.3

# 'agua"limpa'
# Retorna 'agua"limpa'

# """teste 1 2 3 """
# Retorna """teste 1 2 3 """

#3) Determine qual é o resultado dos seguintes cálculos no Python:

# a. Operadores matemáticos
nume1 = 10
nume2 = 3
nume3 = 3.0
nume4 = 13

soma = nume1 + nume2
print(soma)
#13

diferenca = nume1 - nume2
print(diferenca)
#7

multiplicacao = nume1 * nume2
print(multiplicacao)
#30

divisao = nume1 / nume2
print(divisao)
#3.3333333333333335

divisao1 = nume1 / nume3
print(divisao1)
#3.3333333333333335

divisao3 = nume4 / nume2
print(divisao3)
#4.333333333333333

divisao4 = nume4 / nume3
print(divisao4)
#4.333333333333333

divisao_int = nume4 // nume3
print(divisao_int)
#4.0

#b. Ordem dos operadores
nume5 = 5
nume6 = 30
nume7 = 20
num = 2

soma_multi = nume5 + nume6 * nume7
print(soma_multi)
# 605

soma_multi2 = (nume5 + nume6) * nume7
print(soma_multi2)
# 700

soma_multi_div = ((nume5 + nume6) * nume7) / nume1
print(soma_multi_div)
# 70.0

soma_multi_div2 = nume5 + nume6 * nume7 / nume1
print(soma_multi_div2)
# 65.0

#c. Operadores comparação
nume8 = 8
nume9 = 9
nume10 = 4
nume11 = 6
nume25 = 25

menor = num < nume2
print(menor)
# True

maior = nume9 > nume8
print(maior)
#True

igual = n1 == 1
print(igual)
#True

diferente = n1 != num
print(diferente)
#True

diferente1 = n1 != n1
print(diferente1)
#False

menor_igual = nume10 <= nume10
print(menor_igual)
#True

maior_igual = nume5 >= nume11
print(maior_igual)
#False

menor1 = n1 < num < nume2
print(menor1)
#True

menor2 = n1 < num < num
print(menor2)
#False

logica_comparativa = n1 + num < nume25 / nume5
print(logica_comparativa)
#True

#d. Mais operadores matemáticos

exponencial = num ** nume10
print(exponencial)
# 16

gato = 26 % nume5
print(gato)
# 1

#e. Operadores lógicos
gato = 5 not True
print(gato)


#5) Resolva estes problemas em Python, guardando os valores e seus resultados em variáveis diferentes
# a. Calcule a área de um quadrado cujo o lado seja 2cm.


area_quadrado = num ** 2
print(area_quadrado)

#b. Uma mala custa R$ 120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela?
num1 = 120.00

valor_final = num1 - ((num1 / 100) * 5)
print(valor_final)

#c. Um carro está viajando a uma velocidade média de 100 km/h, o trecho de viagem será 200 km. Quantas horas irá demorar a viagem?
velo_media = 100
distancia = 200

hora_total = distancia / velo_media
print (hora_total)

#d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.
pirulitos = [2 , 3 , 1]

total_pirulitos = sum(pirulitos)
print(total_pirulitos)

media_pirulitos = (sum(pirulitos)) / 3
print(media_pirulitos)

#e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi é maior que a idade da sua irmã.

