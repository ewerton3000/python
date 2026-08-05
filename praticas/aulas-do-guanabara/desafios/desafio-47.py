"""Ler vários números e mostrar média, maior e menor valor."""

maior = 0
menor = 7 
numero = 0
media = 0
soma = 0
contador = 0
while contador <= 5 :
    numero = int(input("Digite um número ou digite 0 para parar"))
   
    if numero > maior:
        maior = numero

    if numero == 0 :
        media = soma
        media = media/contador
        break

    elif numero < menor:
        menor = numero
        soma =numero +soma
        
        contador +=1
        
        
print(f"O maior número digitado é : {maior}, o menor numero é : {menor} e a media foi {str(media)[:4]}")
