texto = str(input('Digite seu texto: ')).strip()
print(f'Seu nome em letras maisculas: {texto.upper()}.'
    f'\nSeu nome em minusculas: {texto.lower()}.'
    f"\nSeu nome tem {len(texto)-texto.count(' ')} letras"    
    f'\nSeu primeiro nome é: {texto.split()[0]} e tem {len(texto.split()[0])} letras'
    f'\nSeu nome com todas as primeiras letras maiusculas: {texto.title()}')
