import csv

input_filename = 'Resources/country_info.txt'
countries = {}
with open(input_filename, encoding='utf-8', newline='') as input_file:
    input_file.readline()
    sample = input_file.read(400)
    new_dialect = csv.Sniffer().sniff(sample)
    input_file.seek(0)

    reader = csv.DictReader(input_file, dialect=new_dialect)
    for row in reader:
        name_of_country = row.get('Country')
        countries[name_of_country] = row

for key, values in countries.items():
    print(key, values)
# countries = {}
# with open(input_filename) as country_file:
#     country_file.readline()
#     for row in country_file:
#         data = row.strip('\n').split('|')
#         country, capital, code, code3, dialing, timezone, currency = data
#         # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
#         country_dict = {
#             'name': country,
#             'capital': capital,
#             'country_code': code,
#             'cc3': code3,
#             'dialing_code': dialing,
#             'timezone': timezone,
#             'currency': currency,
#         }
#         # print(country_dict)
#         countries[country.casefold()] = country_dict
#
# # print(countries)
#
# while True:
#     chosen_country = input('Please enter the name of a country: ')
#     country_key = chosen_country.casefold()
#     if country_key in countries:
#         country_data = countries[country_key]
#         print(f"The capital of {chosen_country} is {country_data['capital']}")
#     elif chosen_country == 'quit':
#         break
