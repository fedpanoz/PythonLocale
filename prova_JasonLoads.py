from pathlib import Path
import json
oggetto = Path('listanumeri.json')
da_leggere_noConversion = oggetto.read_text()
print(da_leggere_noConversion)
print(type(da_leggere_noConversion))
da_leggere_converted = json.loads(da_leggere_noConversion)
print(da_leggere_converted)
print(type(da_leggere_converted))