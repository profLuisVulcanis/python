print("\n")
def calcular_notas():
    """
    Calcula as notas de um aluno 
    e informa se o mesmo 
    foi ou não foi aprovado"""

    nome_aluno = input("Digite o nome do aluno: ")

    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        nota4 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Digite um valor numérico, use ponto para separas as cass decimais")
        return #encerra a função se a entrada for inválida
    
    notas = [nota1, nota2, nota3, nota4]

    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)

    print(f"\nNome do aluno: {nome_aluno}")
    print(f"Primeira nota: {nota1}")
    print(f"Segunda nota: {nota2}")
    print(f"Terceira nota: {nota3}")
    print(f"Quarta nota: {nota4}")
    print(f"Media: {media}")
    print(f"Maior nota: {maior_nota}")

    if media >= 6:
        print(f"O Aluno {nome_aluno} foi aprovado")
    else:
        print(f"O Aluno {nome_aluno} foi reprovado")

    print("Fim do programa")
    print("\n")

calcular_notas()
