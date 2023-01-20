from pathlib import Path
def count_words(oggetto):
    try:
        contenuto = oggetto.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'The file {oggetto} does not exist')
    else:
        lista_parole = contenuto.split()
        num_parole = len(lista_parole)
        print(f'The number of words of {oggetto} is {num_parole}')

Lista_libri = ['Alice.txt', 'bellaLi.txt', 'EnglishGrammar.txt', 'Siddhartha.txt', 'Moby_Dick.txt', 'Pocazza_Merda.txt']

for item in Lista_libri:
    oggetto = Path(item)
    count_words(oggetto)