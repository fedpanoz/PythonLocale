import json
from pathlib import Path
import json

oggetto = Path('ListaUtenti')
if oggetto.exists():
    da_leggere = oggetto.read_text()
    da_leggere_conv = json.loads(da_leggere)
    print(f'Hello {da_leggere_conv} you are finally back\n')
else:
    nuovoUtente = input('What is your name?: \n')
    daScrivere = json.dumps(nuovoUtente)
    oggetto.write_text(daScrivere)
    print(f'Hello {daScrivere} we greet you the next time\n')
