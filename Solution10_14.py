from pathlib import Path
import json



def get_dictionary():
    username = input("Tell me what's your user name:\n")
    password = input('Tell me what is your password:\n')
    birth_location = input('Tell me where you were born:\n')

    user_data = {'Username': username, 'Password': password, 'Birth_location': birth_location}

    oggetto = Path('Dizionario.json')
    da_scrivere = json.dumps(user_data)
    oggetto.write_text(da_scrivere)
    print(type(user_data))
    print(type(da_scrivere))
    return user_data


def getting_answer():
    oggetto = Path('Dizionario.json')
    dictio = oggetto.read_text()
    dictio_trsfo = json.loads(dictio)
    answer = input(f"Is {dictio_trsfo['Username']} your real name?: \n")
    if answer == 'yes':
        print(f"Ok, welcome back {dictio_trsfo['Username']}")
    else:
        get_dictionary()

get_dictionary()
getting_answer()



