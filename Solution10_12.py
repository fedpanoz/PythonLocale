from pathlib import Path
import json

def asking_number(oggetto):
    oggetto = Path('Numero_preferito.json')
    num_pref = int((input("Qualè il tuo num preferito?: \n")))
    num_pref_conv = json.dumps(num_pref)
    oggetto.write_text(num_pref_conv)
    return num_pref_conv

def reading_number(oggetto):
    oggetto = Path('Numero_preferito.json')
    da_leggere = oggetto.read_text(encoding='utf-8')
    da_legg_conv = json.loads(da_leggere)
    return da_legg_conv


def greeting_user():
    oggetto = Path('Numero_preferito.json')
    if oggetto.exists():
        print(f'Ben tornato il tuo numero preferito è {reading_number(oggetto)}')
    else:
        print(f'Ok we will greet you the next time and your favourite number is {asking_number(oggetto)}')


greeting_user()