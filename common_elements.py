""" Find two lists common elements"""

import numpy as np

def common(a, b):
    common_list = []
    for el in a:
        if el in b:
            if el not in common_list:
                common_list.append(el)
    return common_list
#return list(set(a).intersection(b)) - in one line :)


a = np.array([1,2,3,2,10,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(common(a,b))
