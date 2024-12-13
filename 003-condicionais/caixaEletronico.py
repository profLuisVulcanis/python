#Exercício de Fixação
saldo = 1000
saque = 500

print("\n")

if saque <= saldo:
    print("Saque realizado com sucesso")
    saldo -= saque #atualiza o saldo
else:
    print("Saldo insuficiente")

print(f"\nSeu saldo atual é de R$ {saldo}.")
print("\n")