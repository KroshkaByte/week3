import csv

new_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', encoding='utf-8', newline="") as lis:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(lis, fields, delimiter=';')
    writer.writeheader()
    for new in new_list:
        writer.writerow(new)