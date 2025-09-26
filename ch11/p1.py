class vector_2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2D vector = [{self.i}i, {self.j}j]")


class vector_3D(vector_2D): 
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"3D vector = [{self.i}i, {self.j}j, {self.k}k]")
a = vector_2D(2, 3)
a.show()
b = vector_3D(5, 6, 8)
b.show()