frase = str(input('Digite um texto: ')).upper()
frase = frase.replace('á', 'a')
print(f"A letra 'a' aparece {frase.count('A')} vezes na frase"
      f"\nA letra 'a' aparece primeiro na posição {frase.find('A')} "
      f"\nA ultima ocorrencia da leta 'a' é na posição {frase.rfind('A')}")



