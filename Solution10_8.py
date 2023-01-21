from pathlib import Path
filenames = ['cats.txt', 'dogs.txt']
for item in filenames:
    try:
        oggetto = Path(item)
        contenuto = oggetto.read_text()
        print(f'The list of {item} is:`\n{contenuto}')
    except FileNotFoundError:
        print(f'i am sorry the file {item} does not exist')



