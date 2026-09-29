"""Crie uma tupla com a classificação dos 20 primeiros colocados do Campeonato Brasileiro e mostre:

Os 5 primeiros.
Os 4 últimos.
Os times em ordem alfabética.
A posição da Chapecoense."""

times=("Flamengo","Palmeiras","Athletico-PR","Fluminense","Bahia",
       "Cruzeiro","Atlético-MG","Coritiba","Bragantino","Santos",
       "São Paulo","EC Vitória","Corinthians","Botafogo","Mirassol",
       "Grêmio","Vasco da Gama","Internacional","Remo","Chapecoense")

for c in range(5):
    print(times[c])
print()
print()
print()
print()
print("Os 4 ultimos times da posição : ")
print()
print()
print("Ultimo time ")

print()
print()
for d in times[-4:]:
      
       print(d)
print()
print()
print()
print("Os times em ordem Alfabética ! ")
print()

print()

ordem = sorted(times)
print(ordem)
print()
print()
print()

ultimo = times.index("Chapecoense")
print(f"Chapecoense está na posição : {ultimo + 1}")



