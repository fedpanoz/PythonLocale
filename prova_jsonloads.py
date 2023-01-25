from pathlib import Path
import json

oggetto = Path('numeri.json')
da_leggere = oggetto.read_text()
print(da_leggere)
print(type(da_leggere))
numeri = json.loads(da_leggere)
print(numeri)
print(type(numeri))