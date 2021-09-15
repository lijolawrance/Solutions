def word_search(doc_list, keyword):
    lst = [ i if doc_list[i].upper().find(keyword.upper()) >0 else 0 for i in range(len(doc_list))]
    print(lst)
    return max(lst)


doc_list1 = ['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']

print(word_search(doc_list1, 'Casinoville?'))
