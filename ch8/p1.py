a = int(input("Entre number :"))
b = int(input("Entre number :"))
c = int(input("Entre number :"))

def max(a,b,c):
    if(a>b and b>c):
        print(f"{a} is greatest")
    elif(b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

max(a,b,c)
