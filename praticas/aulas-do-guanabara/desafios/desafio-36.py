"""Leia uma frase e informe se ela é um palíndromo, desconsiderando os espaços."""
frase = input("Digite uma frase ou palavra")
frase = frase.replace(" ","").lower()
invertida = ""

for letra in frase:

        invertida = letra + invertida
        
if frase == invertida:
    print("Palíndromo")

else:
      print("Não é um palíndromo")