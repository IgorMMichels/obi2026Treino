idadeMae = int(input('Idade da Mônica: '))
idadeUm = int(input('Idade Primeiro: '))
idadeDois = int(input('Idade Segundo: '))
idadeTres = int(idadeMae-idadeUm-idadeDois)

idades = [idadeUm, idadeDois, idadeTres]

idadeMaior = max(idades)

print(int(idadeMaior))