class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return number(self.n + num.n)
    
a = number(1)
b = number(2)
c = number(3)
res = a + b + c
print(res.n)