from pathlib import Path
import json
oggetto = Path('ListaNomiUser.json')
da_legg = oggetto.read_text()
da_legg_conv = json.loads(da_legg)
print(f' Hello this is the list of users {da_legg_conv}')