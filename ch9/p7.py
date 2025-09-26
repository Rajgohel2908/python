with open("log.txt", "r") as f:
    para = f.readlines()

lineno = 1
for line in para:
    if("python" in line):
        print(f"Its talking about python on line no :{lineno}")
        break
    lineno += 1
else:
    print("Its not talking about python")