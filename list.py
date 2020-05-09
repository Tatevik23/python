""" You are given a list of characters. Find the least popular character in the list.
Return number of occurrences of the least popular character and the list of
characters that have occurred that many times."""

def least_pop_element(char):
    res = {}
    min_val_el = []
    for keys in char:
        res[keys] = res.get(keys, 0) + 1
    min_count = min(res.values())
    for i,j in res.items():
        if j == min_count:
            min_val_el.append(i)
    print("MIN_VAL_LIST: ", min_val_el, "\n", "DICT: ", res)
    return min_count, min_val_el

char = ["a","d", "h", "s", "a", "d"]
print(least_pop_element(char))


