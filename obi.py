N = [int(x) for x in input().split()]

convidados = 0

for i in range(N[0]):
    notas = [int(x) for x in input().split()]
    somaN = notas[0] + notas[1]
    if somaN >= N[1]:
        convidados += 1
        
        
print(convidados)