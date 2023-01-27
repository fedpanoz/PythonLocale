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

def get_new_username(user_data):
    new_user = input('Ok tell me your username please:\n')
    user_data['Username'] = new_user
    answer = input(f"Is {user_data['Username']} your current username?: \n")




