from pathlib import Path
answer = input("What is your name?\n")
oggetto = Path("guest.txt")
oggetto.write_text(answer)
