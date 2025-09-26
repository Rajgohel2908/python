from functools import reduce

l = [45,5634,244345,5643,2434,45475646]

def max(a,b):
    if a>b:
        return a
    return b

print(reduce(max,l))