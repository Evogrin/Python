from unidecode import unidecode
a = str(input('Digite uma frase: ')).strip().upper()
b = unidecode(a)
print(f'A letra "a" aparece {b.count("A")} vezes')
print(f'A letra "a" aparece a primeira vez na posição {b.find("A") + 1}')
print(f'A ultima letra "a" aparece na {b.rfind("A") + 1}')