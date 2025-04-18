#TUPLE
user = ("jan", "kowalski", 10)
city  = "Warszawa", "Polska"
# print(city)

info = user + city #konkatenacja
# print(info)

nums = (1,2,3)
nums_multiply = nums * 4
counter = nums_multiply.count(3)
# print(counter)
# print(nums_multiply)

host, port, https = ("host.pl", 4055, True)
# print(host)
# print(port)

user = ("Jan", "kowalski", 10)
is_valid = 3 in user
is_john = "Jan" in user
# print(is_john)

#SET
my_set = {3,6,7,8}
# my_set.pop()
# print(my_set)

cities1 = {"Ełk", "Ełk", "Kraków", "Katowice", "Berlin"}
cities2 = {"Milan", "Berlin"}

all = cities1 | cities2 #połączenie
all2  = cities1.union(cities2)
print(all2)

common1 = cities1 & cities2 #wspólny element
common2 = cities1.intersection(cities2)
print(common2)

diff = cities1 - cities2
diff2 = cities1.difference(cities2)
print(diff2)

symmetric = cities1 ^ cities2 #wyrzuca element który jest w obu
print(symmetric)