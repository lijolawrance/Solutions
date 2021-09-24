import re
from typing import Dict


def lst():
    mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(mylist[4:9])
    print(mylist[::-1])
    print(mylist[::2])
    set1 = set(mylist)
    list1 = ["Hello", "Hi", "Greetings", "Cheers", "Hi", "hello", "Greetings!"]
    print(len(set(list1)))


def st():
    set1 = {26, 200, 2001, 92, 550, 2001, 338, 92.0, 11}
    print(len(set1))
    if (11 in set1) and (52 / 2 in set1):
        print(True)
    set1.add(550)
    print(len(set1))
    set1.remove(550)
    print(len(set1))
    set1.pop()
    print(len(set1))

    set1 = {26, 200, 2001, 92, 550}
    set2 = {334, 92, 29, 650, 550, 25, 1002}
    print(set1.difference(set2))
    print(set1.intersection(set2))
    set2.discard(26)
    print(set2)
    return set2


def tple():
    mytuple = (100, 250, 300, 450, 500, "Python", "Java", "C++", 250)
    print(mytuple[0:3])
    print(mytuple[7:])
    print(mytuple[-5:-2])

    '''mytuple = (100, 250, 300, 450, 500)
    (a, b, c, d, e) = mytuple
    print((10 % e))'''

    print((mytuple + (200, 900 // 2)).count(450))
    print((mytuple + (410, 430, 450, 205 * 2, 900 // 2, 445)).count(450))
    print(mytuple[1::3])
    print(mytuple.index(250))


def rnge():
    myrange = range(10, 16, 2)[::-1]
    # myrange = range(2,20,3)
    print(list(myrange))
    print(tuple(myrange))


def dct():
    ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M",
                    "Hungary": "9.6M", "Moldova": "4.1M"}

    print(float(ee_countries["Moldova"].rstrip("M")))
    # print(frozenset(ee_countries))
    print(ee_countries)
    ee_countries["Estonia"] = "28.1M"
    print(max(ee_countries.keys()))
    # del ee_countries["Estonia"]
    print(min(ee_countries.items()))
    print(ee_countries.get("Ukraine"))
    ee_countries.update([["India", "9.6M"], ["China", "54M"]])
    # ee_countries.popitem()
    print(len(ee_countries.items()))
    print(sorted(ee_countries.keys(), reverse=True)[1])
    # test = {['Ukraine', 'Poland', 'Romania']: [43.7, 38.1, 19.5]}


def conv():
    print(bin(3))
    print(int('0011', 2))


def if_else():
    mystring = "Solving Python quizzes is awesome. Can I have more, please?"

    if mystring[5:8].startswith("i") and (mystring[::2][2] == "i"):
        print("Great job!")
    elif "a" in mystring[-7:-4] or mystring[-2:] == "e?":
        print("Great job once again!")
    else:
        print("Great job again!")

    mynum = 2500

    if mynum % pow(5, 2) < 100:
        print("Awesome!")
    elif abs(10 % 2 - mynum) < 2019:
        print("Amazing!")
    elif type(mynum / 50) is not int:
        print("Cool!")
    else:
        print("Whatever!")

    if mynum % abs(-mynum // 100) > 100:
        print("Awesome!")
    elif max(mynum % 250, mynum % 500) == 0:
        print("Amazing!")
    elif type(mynum / 50) is not int:
        print("Cool!")
    else:
        print("Whatever!")

    if bool():
        print(True)


def fn():
    x = [1, 2]
    y = [10, 100]

    for i in x:
        # print(i)
        for j in y:
            # print(j)
            if i % 2 == 0:
                print(x[1] * y[1])


def exp():
    x = [1, 9, 17, 32]

    try:
        print(x[3] % 3 ** 5 + x[4])
    except ZeroDivisionError:
        print("Zero!")
    else:
        print("Clean!")
    finally:
        print("Finish!")


def fl():
    f = open("text.txt", "w")
    f.write('scala')
    f.close()

    with open("text.txt", "w") as f:
        f.write('python')
        f.close()
    f = open("text.txt", "r")
    print(f.read())
    f.close()


def regexgrp():
    s = "Bitcoin has born on Jan 3rd 2009 as an alternative to the failure of the current financial system." \
        " In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
    result = re.match("Bitcoin", s, re.IGNORECASE)
    try:
        result = re.match(r"B.{6} w.{3}", s)
        print(result.group())
    except AttributeError:
        print('not found')
    result = re.search(r"(\d{4})\s", s)
    print(result.group())


def lst_comp():
    cph = [i ** 2 for i in range(5, 25, 3) if i <= 15]
    print(cph)


def dict_comp():
    cph = {x: x * 3 for x in range(9)}
    print(cph)


def set_comp():
    cph = {x / 2.5 for x in range(10, 19)}
    print(cph)


def lambda_fn():
    lam = lambda list1: [x * y for x in range(1, 5) for y in list1]
    print(lam([1, 2]))


def lst_concat():
    import itertools

    list1 = [1, 2, 3]
    list2 = [4, 5]

    result = list(list1+list2)

    print(result)


if __name__ == "__main__":
    lst_concat()
