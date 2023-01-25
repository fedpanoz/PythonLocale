from pathlib import Path
import json



def get_stored_name(oggetto):
    oggetto = Path('ListaUtenti2')
    da_leggere = oggetto.read_text()
    da_leggere_conv = json.loads(da_leggere)
    print(f'welcome back {da_leggere_conv}')



def insert_new_name(oggetto):
    oggetto = Path('ListaUtenti2')
    nuovo_utente = input('What is your name?: \n')
    da_scrivere = json.dumps(nuovo_utente)
    oggetto.write_text(da_scrivere)
    print(f'Hello {da_scrivere} we salute the next time you will be back\n')

def greeting_user():
    oggetto = Path('ListaUtenti2')
    if oggetto.exists():
        get_stored_name(oggetto)
    else:
        insert_new_name(oggetto)


greeting_user()