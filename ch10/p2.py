class calculator:
    def __init__(self,n):
        self.square = n*n
        self.root = n ** 0.5
        self.cube = n*n*n
 
n = calculator(9)
print(f"square :{n.square}\ncube :{n.cube}\nsquare root :{n.root}")
