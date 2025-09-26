class complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, b):
        return complex(self.r + b.r, self.i + b.i)
    
    def __mul__(self, b):
        real = self.r * b.r - self.i * b.i
        imag = self.r * b.i + self.i * b.r
        return complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"

a = complex(3, 4)
b = complex(4, 5)
print(a + b)
print(a * b)