N = [int(x) for x in input().split()]



for i in range(N[0]):
    refeicao = [int(x) for x in input().split()]
    N[1] -= (refeicao[0]*4)
    N[1] -= (refeicao[1]*9)
    N[1] -= (refeicao[2]*4)
    
input(N[1])