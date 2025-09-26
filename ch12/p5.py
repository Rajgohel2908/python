with open('table.txt','a') as f:
    n = int(input("Enter number :"))
    f.write(f"\nTable of {n}:\n")
    table = [f.write(f"{n} X {i} = {i*n}\n") for i in range(1,11)]