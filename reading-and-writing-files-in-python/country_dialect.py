import csv

input_filename = 'Resources/country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""                         # initializing a sample string
    for line in range(3):               # specifying 3 lines to read
        sample += countries_data.readline()         # concatenate
    # sample = countries_data.read(int(150))    # reading 150 chars of file
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*'*80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
