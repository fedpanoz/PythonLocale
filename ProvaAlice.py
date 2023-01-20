from pathlib import Path
oggetto = Path('Alice.txt')
try:
    contenuto = oggetto.read_text(encoding='utf-8')
except FileNotFoundError:
    print('Sorry th e file is not there')
else:
    parole = contenuto.split()
print(type(parole))
print(len(parole))
