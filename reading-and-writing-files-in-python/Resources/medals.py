import csv


csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f'Column headers: {headers}')
    reader = csv.reader(csv_file)
    csv_int_list = []
    for row in reader:
        # print(row)
        rank, country, gold, silver, bronze, total = row
        print(int(rank), country, int(gold), int(silver), int(bronze), int(total))

# print(csv_int_list)
