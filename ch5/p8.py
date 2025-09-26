# if the language of two friends are same then it will not change the value ad will print it again
a = {}

name = input("Enter name:")
lang = input("Enter language:")
a.update({name : lang})
name = input("Enter name:")
lang = input("Enter language:")
a.update({name : lang})
name = input("Enter name:")
lang = input("Enter language:")
a.update({name : lang})
name = input("Enter name:")
lang = input("Enter language:")
a.update({name : lang})

print(a)