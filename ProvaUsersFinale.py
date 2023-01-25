from pathlib import Path
import json

oggetto = Path('users_finale')

if oggetto.exists():
    da_leggere = oggetto.read_text()
    da_leggere_conv = json.loads(da_leggere)
    print(f'Hello {da_leggere_conv} welcome back')
else:
    tuo_nome = input('Come ti chiami? \n')
    tuo_nome_conve = json.dumps(tuo_nome)
    da_scrivere = oggetto.write_text(tuo_nome_conve)
    print(f'Hi {tuo_nome} we remember you the next time')