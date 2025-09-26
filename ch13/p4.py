def div(n):
    if n%5==0:
        return True
    return False

l = [1,3,5,15,20,24,35]

f = list(filter(div,l))
print(f)