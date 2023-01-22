from pathlib import Path

letture = ['Alice.txt', 'Moby_Dick.txt', 'siddhartha.txt']
try:
    for item in letture:
        oggetto = Path(item)
        letto = oggetto.read_text(encoding='utf-8')
        numbr = letto.count('the')
        print(numbr)
except FileNotFoundError:
    print('i am sorry your file does not exist')