from pathlib import Path
filenames = ['cats2.txt', 'dogs.txt']
for item in filenames:
    try:
        oggetto = Path(item)
        contenuto = oggetto.read_text()
        print(f'The list of {item} is:`\n{contenuto}')
    except FileNotFoundError:
        pass



