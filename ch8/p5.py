'''
***
**     n=3
*


'''

n = int(input("Enter number of rows :"))

def pat(n):
    if(n==0):
        return 1
    print("*"*n,)
    return pat(n-1)
pat(n)