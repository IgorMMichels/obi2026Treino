N = int(input())
P = int(input())
full = 1
dias = 0

while (full * P) <= N:
    full = full * P
    dias += 1

print(dias)
