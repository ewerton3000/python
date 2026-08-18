"""Crie um programa que leia a idade e o sexo de várias pessoas.

Ao final, informe:

Quantas pessoas têm mais de 18 anos.
Quantos homens foram cadastrados.
Quantas mulheres têm menos de 20 anos."""

arraynome = []
arrayidade = []
arraysexo = []
arraynomemaior = []
arrayidademenorf = []
arraymenoresde20 = []
arrayidademenorq20 =[]
homens = []
mulheres = []
c = ''
while True :
    nome = input("Digite um nome :  ")
    arraynome.append(nome)
    idade = int(input("Digite a sua idade :  "))
    arrayidade.append(idade)
    sexo = input("Digite o seu sexo :   ")
    arraysexo.append(sexo)

    if idade >= 18:
        arraynomemaior.append(nome)
        

    if sexo in ("h" , "homen", "masculino", "m"):
        homens.append(sexo)

    elif sexo in ( "mulher", "feminino","f"):
                mulheres.append(sexo)

    if idade < 20 and sexo in ("m" , "mulher", "feminino","f"):
        arraymenoresde20.append(nome)

    c = input("Deseja continuar ?  ")
        

    if c == "nao":
                break
        
print(f"As pessoas maiores de 18 anos são : {arraynomemaior}")

print(f"O total de homens cadastrados foi  {len(homens)}")

print(f"O total de mulheres cadastrados foi  {len(mulheres)}")

print(f"As pessoas menores de 20 anos são :   {len(arraymenoresde20)}")



