from pathlib import Path
oggetto = Path('bellaLi.txt')
try:
    print(oggetto.read_text(encoding='utf-8'))
except FileNotFoundError:
    print('Your file does not exist')
else:
    print("\n\n\nOk you have done it")
