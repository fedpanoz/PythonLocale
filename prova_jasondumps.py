from pathlib import Path
import json

esempio = [2, 45, 65, 9, 4, 10]

oggetto = Path('numeri.json')
da_scrivere = json.dumps(esempio)
oggetto.write_text(da_scrivere)

print(type(da_scrivere))