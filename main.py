#1
name = 'Jan'
surname = 'Kowalski'
city = 'Poznań'
print(f'To jest {name} {surname}. Jego miejsce urodzenia to {city}.')


#2
result2 = 'to jest krótkie zdanie na temat Jana'.replace(" ","-")
print(result2)

#3
greeting = "hello, world!"
length = len(greeting)
print(length)

greeting2 = greeting.upper()
print(greeting2)

greeting3 = greeting.capitalize()
print(greeting3)

#4
movie = "lord of the rings"
movie2 = movie.title()
print(movie2)

#5
movie2 = "dzisiaj jest sobota"
movie5ch = movie2[4]
print(movie5ch)


#dodatkowe 1
sentence = "Ala ma kota"
reversed_text = sentence[::-1]
print(reversed_text)

#dodatkowe 2
phrase = 'Litwo, ojczyzno moja, ty jesteś jak zdrowie'
count_o = phrase.count("o")
print(count_o)


