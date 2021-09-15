'''fact = "Romania is the home of the heaviest building in the world, the Palace of Parliament in Bucharest."
h='heaviest'
fact1 = "Romania is the home of the {0} building in the world, the Palace of Parliament in Bucharest."
print(fact1.format(5))
print(fact.index('he'))

print(fact.index("he") * fact.count("P"))

print(fact.split(" ")[7].upper())
print('%'.join(fact.split(" ")[-1].strip('.')))

a = "Hi"
b = "Hello"
print(((a + b) * 5))
print(((a + b) * 5).find("Hello"))
a = (25 % 9) * 10
x = 150 + 3 ** 3 % (18 % 5)
y=(25 % 5 == 33 % 11) and (10 ** 3 >= 300)
print(y)
print(bool("I love Python"))
'''

mylist = ["Europe", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]
print((mylist))
list1 = [10, 211, 99.99, 50.75, 11.5]
print(sorted(list1, reverse=True)[1])
print(sorted(list1))