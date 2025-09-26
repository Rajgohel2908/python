class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,other):
        result = vector(self.i + other.i, self.j + other.j, self.k + other.k)
        return result
    
    def __mul__(self,other):
        result = (self.i * other.i + self.j * other.j + self.k * other.k)
        return result
    
    def __str__(self):
        return f"vetor:({self.i}, {self.j}, {self.k})"
    
a = vector(1,2,3)
b = vector(5,6,7)
c = vector(4,8,5)
print(a+b)
print(a*b)

print(a+c)
print(a*c)