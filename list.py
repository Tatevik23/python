"""import operator
   # using operator lib
str_list = ["a", "b", "c", "a", "b"]
print("LIST: ", str_list)
res = {}
for keys in str_list:
    res[keys] = res.get(keys, 0) + 1
    #print(res[keys])
    if (res[keys] < 2):
       print(res[keys])
print ("Count of all characters: \n" +  str(res))
print("MIN: ", min(res.items(), key=operator.itemgetter(1))[0])"""

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


