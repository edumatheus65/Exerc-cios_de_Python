#galera = [['João', 19], ['Maria', 22], ['Roberto', 33]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')

    print(f'{galera[0][0]} tem {galera[0][1]} anos')
