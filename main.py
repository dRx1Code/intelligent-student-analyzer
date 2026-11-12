# nivel 1

print("=== Sistema de Notas - Nível 1 ===")

nota1 = float(input("Digite a 1ª nota (0 a 10): "))
nota2 = float(input("Digite a 2ª nota (0 a 10): "))
nota3 = float(input("Digite a 3ª nota (0 a 10): "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nA média final foi: {media:.2f}")

if media >= 6.0:
    print("Status: Aluno APROVADO! 🎉")
else:
    print("Status: Aluno REPROVADO. ❌")