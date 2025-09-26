class employee:
    salary = 10000
    
    @property
    def salaryafterincrement(self):
        return self.salary + self.salary * (self.increment / 100)
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100

e = employee()
e.salaryafterincrement = 14500
print(e.salaryafterincrement,e.increment)