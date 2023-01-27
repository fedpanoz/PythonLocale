from pathlib import Path
import json

oggetto = Path('Dizionario.json')
da_leggere = oggetto.read_text()
da_leggere_conv = json.loads(da_leggere)
print(da_leggere_conv)

print(type(da_leggere))
print(type(da_leggere_conv))
print(len(da_leggere_conv))
for item in da_leggere_conv:
    print(da_leggere_conv[item])
for x, y in da_leggere_conv.items():
    print(f'{x},    {y}\n')