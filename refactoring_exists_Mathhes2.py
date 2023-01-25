from pathlib import Path
import json
def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    username = input("Waht is your username:? \n")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f'Welcome back {username}!\n')
    else:
        username = get_stored_username()
        print(f'We will remember {username}, next time you came back\n')


greet_user()