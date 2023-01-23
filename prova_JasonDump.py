from pathlib import Path
import json

numeri = [3, 45, 65, 33, 7, 8, 4]
oggetto = Path('listanumeri.json')
numeriConverted = json.dumps(numeri)
da_scrivere = oggetto.write_text(numeriConverted)