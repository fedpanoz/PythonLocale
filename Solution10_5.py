from pathlib import Path
guests = []

flag = True
while flag:
    answer = input("Do you want to became guest? \n")

    if answer == 'yes':
        ospite = input("What's your name?:\n")
        guests .append(ospite)
    elif answer == "no":
        flag = False

stringa_ospiti = ''
for item in guests:
    stringa_ospiti += f"{item}\n"
oggetto = Path("guest_book.txt")
oggetto.write_text(stringa_ospiti)


