from pathlib import Path
import json

username = input("Tell me what's your user name:\n")
password = input('Tell me what is your password:\n')
birth_location = input('Tell me where you were born:\n')

user_data = {'Username': username, 'Password': password, 'Birth_location': birth_location}

oggetto = Path('Dizionario.json')
da_scrivere = json.dumps(user_data)
oggetto.write_text(da_scrivere)
print(user_data['Username'])
