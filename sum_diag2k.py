""" Find diagonal elements sum of random matrice """

import numpy as np
def diag_2k(arr):
    result = 0
    if (len(arr) == len(arr[0])): # rows and columns elements count also can be check - arr.shape[0], arr.shape[1]
        print("Matrice shape is: ", arr.shape)
        for i in range(len(arr)):
            result = result + arr[i][i]
    else:
        return 0
    return result

arr = np.random.randint(0,20,size = (3,1))
print("Matrice", arr)
print("Sum of diagonal elements: ", diag_2k(arr))
