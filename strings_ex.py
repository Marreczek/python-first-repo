firstname = 'Anna'
city = "Warszawa"
street = 'Krakowska'
address = city + ", " + street
print(address)

result4 = f"To jest {firstname}. Jej miejsce urodzenia to {city}."
print(result4)

result5 = "To jest %s. Jej miejsce urodzenia to %s." % (firstname,city)
print(result5)

result6 = 'To jest {}. Jej miejsce urodzenia to {}.'.format(firstname, city)
print(result6)

content = ' hasło '.strip()
length = len(content)
print(length)