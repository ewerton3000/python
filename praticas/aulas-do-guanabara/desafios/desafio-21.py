"""Leia a nota de um aluno.
Nota maior ou igual a 7 → Aprovado.
Nota entre 5 e 6,9 → Recuperação.
Nota menor que 5 → Reprovado."""

nota = float(input(" Digite a sua nota : "))

if nota >=7:
    print("Aprovado")
elif nota >=5 and nota <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")