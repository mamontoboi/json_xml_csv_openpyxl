# Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів.
# Зареєструйте створені діалекти та попрацюйте, використовуючи їх зі створенням/читанням файлом.

import csv


class CustomDialect1(csv.Dialect):
    quoting = csv.QUOTE_NONE
    quotechar = ""
    delimiter = "\t"
    lineterminator = '\n'
    escapechar = '.'


csv.register_dialect('tester_1', CustomDialect1)

with open('deniro.csv', 'r') as file:
    reader = csv.reader(file)

    with open('new_deniro.csv', 'w') as new_file:
        writer = csv.writer(new_file, dialect='tester_1')

        for line in reader:
            writer.writerow(line)


class CustomDialect2(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = '#'
    delimiter = 'X'
    lineterminator = '\n'


csv.register_dialect('tester_2', CustomDialect2)

with open('deniro.csv', 'r') as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
    with open('dict_file.csv', 'w') as dd:
        writer = csv.DictWriter(dd, dialect='tester_2', fieldnames=['Year', 'Rating', 'Title'])
        writer.writeheader()
        writer.writerow({
            'Year': 1968,
            'Rating': 86,
            'Title': "Greetings"
        })
