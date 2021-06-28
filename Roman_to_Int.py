def romanToInt( s):
    int_value = max_local = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for char in reversed(s):
        con_val = roman_dict[char];
        if max_local <= con_val:
            int_value += con_val
            max_local = con_val
        else:
            int_value -= con_val
    return int_value


print(romanToInt('II'))
