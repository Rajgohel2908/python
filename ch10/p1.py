class programmer:
    company = "Microsft"
    def __init__(self, name, salary, language):
        self.name = input("Enter name :")
        self.salary = int(input("Enter salary"))
        self.language = input("Enter language")
        
e1 = programmer("Raj", 120000, "python")
print(e1.company, e1.name, e1.salary, e1.language)
e2 = programmer("Rajveer", 110000, "JavaScript")
print(e2.company, e2.name, e2.salary, e2.language)
e3 = programmer("Om", 100000, "C++")
print(e3.company, e3.name, e3.salary, e3.language)