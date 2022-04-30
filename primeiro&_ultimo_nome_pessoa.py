nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras'
      f'\nSeu ultimo nome é {nome.split()[-1]} e tem {len(nome.split()[-1])} letras')
