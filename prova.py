import json

def write_dict_to_file(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    user_data = {}
    user_data['name'] = input("Enter name: ")
    user_data['occupation'] = input("Enter occupation: ")
    user_data['birth place'] = input("Enter birth place: ")

    file_path = input("Enter file path: ")
    write_dict_to_file(user_data, file_path)
    print(f"Data written to {file_path}")

write_dict_to_file()