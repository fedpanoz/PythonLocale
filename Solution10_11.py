from pathlib import Path
import json
favorito = int(input('What is your favorite number:?\n'))
oggetto = Path('Numero_favorito.json')
Num_conv = json.dumps(favorito)
oggetto.write_text(Num_conv)
print(type(Num_conv))
print(Num_conv)
print(type(int(Num_conv)))
print(int(Num_conv))