K = [int(x) for x in input("").split()]
N = [int(x) for x in input("").split()]

corte = 100

for i in range(corte):
    corte = corte - 1
    aprovado = 0
    for i in N:
        if i >= corte:
            aprovado += 1
            if aprovado == K[1]:
                break
    if aprovado == K[1]:
        break

print(corte)
