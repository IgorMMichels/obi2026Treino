X = int(input(''))
N = int(input(''))

Sx = X*N

for i in range(N):
    M = int(input(''))
    Sx -= M
    
print(Sx + X)