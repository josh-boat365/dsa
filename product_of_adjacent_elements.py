"""_summary_
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""


def prod_of_adj_elem(array):
    res = max(a *b for a , b in zip(array, array[1:]))
    
    return res

#Test case 
array = [1,2,3,4,5,6,7]
print(prod_of_adj_elem(array))