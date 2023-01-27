import os

# Prompt the user for input
username = input("Enter your username: ")
password = input("Enter your password: ")
birth_location = input("Enter your birth location: ")

# Create a dictionary to store the information
data = {"username": username, "password": password, "birth_location": birth_location}

# Write the dictionary to a file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "My_info.txt")
with open(file_path, "w") as f:
    f.write(str(data))

print("User data has been saved to file.")
