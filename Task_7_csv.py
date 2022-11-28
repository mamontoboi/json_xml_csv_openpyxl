# Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль.
# Файл має містити такі стовпчики: імена, прізвища, дати народження та місто проживання.
# Реалізуйте можливості перезапису цього файлу, додавання нових рядків до наявного файлу,
# рядкового читання з файлу та конвертації всього вмісту у формати та JSON.

import csv
import re
import json

fieldnames = ['first name', 'last name', 'DOB', 'place of residence']


class CustomDialect(csv.Dialect):
    delimiter = '\t'
    quoting = csv.QUOTE_NONE
    lineterminator = '\n'


csv.register_dialect('tab_dial', CustomDialect)


def operation_with_file():
    global writer
    while True:
        data = {}
        data['first name'] = input('First name: ').title()
        data['last name'] = input('Last name: ').title()
        dob = input('Date of birth: ')
        data['DOB'] = re.sub(r'[,./-]', '/', dob)
        data['place of residence'] = input('Place of residence: ').title()
        writer.writerow(data)
        choice = input('Do you want to continue updating a database? (y/n)\n').lower()
        if choice == 'y':
            continue
        else:
            break


def write_database_first_time():
    global writer
    with open('database.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, dialect='tab_dial')
        writer.writeheader()
        operation_with_file()


def update_database():
    global writer
    with open('database.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, dialect='tab_dial')
        operation_with_file()


def read_file():
    with open('database.csv', 'r') as file:
        reader = csv.DictReader(file, dialect='tab_dial')
        for line in reader:
            print(line)


def dump_into_json():
    with open('database.csv', 'r') as file:
        reader = csv.DictReader(file, dialect='tab_dial')
        with open('json_db.json', 'w') as j_file:
            for line in reader:
                json.dump(line, j_file, indent=4)
                jdata = json.dumps(line, indent=4)
                print(jdata)


def menu():
    while True:
        action = input("""
        What do you want to do with database file:
        1 - create new file
        2 - append existing file
        3 - read data from file
        4 - convert data into json file 'json_db.json
        5 - quit the programme\n""")
        match action:
            case '1':
                write_database_first_time()
            case '2':
                update_database()
            case '3':
                read_file()
            case '4':
                dump_into_json()
            case '5':
                break
            case _:
                continue


if __name__ == '__main__':
    menu()
