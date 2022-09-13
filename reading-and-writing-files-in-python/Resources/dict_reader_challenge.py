import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'


countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # read the header row, parse it, and convert the headers to lowercase.
    new_headers = country_file.readline().lower().strip().split(dialect.delimiter)

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=new_headers)



    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country.casefold() == 'quit':
        break
