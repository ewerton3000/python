"""Crie uma tupla com a classificação dos 20 primeiros colocados do Campeonato Brasileiro
e mostre algumas informações sobre ela.

"""

times=("Brasileirão times","Flamengo","Palmeiras","Athletico-PR","Fluminense","Bahia",
       "Cruzeiro","Atlético-MG","Coritiba","Bragantino","Santos",
       "São Paulo","EC Vitória","Corinthians","Botafogo","Mirassol",
       "Grêmio","Vasco da Gama","Internacional","Remo","Chapecoense")

print("======= BRASILEIRÃO ========")
for posicao, times in enumerate(times[1:], start=1):
   

    print(posicao, times)