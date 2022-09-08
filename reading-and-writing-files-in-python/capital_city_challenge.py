from countries import *

selected_country = input("What country would you like to know the capital of?\n").casefold()

if selected_country in countries:
    selected_country_dict = countries[selected_country]
    selected_country_capital = selected_country_dict['capital']
    if selected_country_capital != '':
        print(f'The capital of {selected_country_dict["name"]} is {selected_country_capital}')
    else:
        print(f"{selected_country_dict['name']} doesnt actually have a capital.")
else:
    print("I don't seem to have any information on that. Maybe check your spelling?")
