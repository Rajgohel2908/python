a = ["apple", "banana", "pineapple", "grapes"]

def remove_and_strip(a ,word):
    l = []
    for item in a:
        if(item != word):
            l.append(item.strip(word))
    return l

print(remove_and_strip(a, "le"))