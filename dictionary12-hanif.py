myDict = {'name': 'Edy', 'age': 26}   # Dictionary awal

print(myDict.items())     # Output: dict_items([('name', 'Edy'), ('age', 26)])
print(myDict.keys())      # Output: dict_keys(['name', 'age'])
print(myDict.values())    # Output: dict_values(['Edy', 26])

print(myDict.popitem())   # Output: ('age', 26)
print(myDict)             # Output: {'name': 'Edy'}