def restoreString(s, indices) :
    #lst=[s[i] for i in indices]
    #return lst
    lst_shf_string = [None for i in range(len(s))]
    for i in range(len(s)):
        lst_shf_string[indices[i]] = s[i]
    return ''.join(lst_shf_string)

s="codeleet"
indices =[4,5,6,7,0,2,1,3]

print(restoreString(s,indices))