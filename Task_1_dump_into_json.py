# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.

import json

data = {
    "first name": "Gustavus",
    "last name": "Adolfus",
    "country": "Sweden",
    "occupation": [
        "king",
        "general",
    ],
    "alias": "the Lion of the North"
}

json_data = json.dumps(data, indent=4)
print(json_data)


with open('The_King.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('The_King.json', 'r') as file:
    new_data = json.load(file)

print(new_data)

data = {
    "first name": "Armand",
    "last name": "Richelieu",
    "country": "France",
    "occupation": [
        "cardinal",
        "first minister"
    ],
    "alias": "the Red Eminence"
}

with open('The_King.json', 'a') as file:
    file.seek(2)
    file.write("\n" + "=" * 30 + "\n")
    json.dump(data, file, indent=4)


file = open('The_King.json', 'r')
for line in file:
    print(line, end='')
