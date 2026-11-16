print("=== Sistema de Notas - Nível 2 ===")

while True:
    nome = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        print("Encerrando o sistema...")
        break

    soma_notas = 0
    for i in range(1, 4):
        while True:
            nota = float(input(f"Digite a {i}ª nota de {nome}: "))
            if 0 <= nota <= 10:
                soma_notas += nota
                break
            else:
                print("Nota inválida. Por favor, digite um valor entre 0 e 10.")

    media = soma_notas / 3
    print(f"\nMédia de {nome}: {media:.2f}")
    
    if media >= 6.0:
        print("Status: Aluno APROVADO! 🎉")
    else:
        print("Status: Aluno REPROVADO. ❌")