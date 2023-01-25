from pathlib import Path
import json

user_name = input("Tell me what's your name")
oggetto = Path('ListaNomiUser.json')
da_scrivere = json.dumps(user_name)
oggetto.write_text(da_scrivere)
