from unidecode import unidecode
sentence = str(input('Type a sentence: ')).lower().strip()
cleansentence = unidecode(sentence)
letter = str(input("Which letter you're looking for?"))
print('The letter {} showed {} times.'.format(letter.upper(), cleansentence.count(letter)))
print('First letter {} showed at position number {}'.format(letter.upper(), cleansentence.find(letter) + 1))
print('Last letter {} showed at position number {}'.format(letter.upper(), cleansentence.rfind(letter) + 1))