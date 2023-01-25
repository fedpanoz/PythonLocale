from pathlib import Path
import json
oggetto = Path('Numero_favorito.json')
da_leggere = oggetto.read_text()
convertito = json.loads(da_leggere)
print(f'I know your favorite number is  {convertito}\n')
print(type(convertito))