
def cryptofy(key:list):
    new_key = []
    for item in key:
        if item == str():
            item +="abnd"
        elif item == int():
            item += "124"
        new_key.append(item)
    return new_key

lista = [1,24,566,"sfnhjks0","1248742jhkfs",124,53,5555,"tjkb"]
test = cryptofy(list)
print(test)        