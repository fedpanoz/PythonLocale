from pathlib import Path
oggetto = Path('guest_book.txt')
print(oggetto.read_text(encoding='utf-8'))