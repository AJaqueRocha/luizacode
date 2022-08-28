#5) Resolva estes problemas em Python, guardando os valores e seus resultados em variáveis diferentes
# a. Calcule a área de um quadrado cujo o lado seja 2cm.
num = 2

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
davi = 13
irma_davi = 7
