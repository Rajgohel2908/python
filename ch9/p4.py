def replace():
    para = ""
    with open("para.txt","r") as f:
        para = f.read()
    para = para.replace("donkey" , "######")

    with open("para.txt","w") as f:
        f.write(para)
        
replace()