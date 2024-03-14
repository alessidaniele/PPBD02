saldo_iniziale= 1000
INTERESSE = 1.10
interesse1 = saldo_iniziale * INTERESSE
interesse2 = interesse1 * INTERESSE
interesse3 = interesse2 * INTERESSE

print("saldo iniziale è:" , saldo_iniziale)
print("saldo al secondo anno è:" , interesse1)
print("saldo al terzo anno è:" , interesse2)
print("saldo al quarto anno è:" , interesse3)

saldo_finale = saldo_iniziale * INTERESSE ** 3
print(saldo_finale)




