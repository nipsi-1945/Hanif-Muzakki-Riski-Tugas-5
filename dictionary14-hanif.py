myDict = {'name': 'Edy', 'age': 26}     # Dictionary awal

newDict = {'a':1, 'b':2, 'c':3}         # Dictionary baru
myDict.update(newDict)                  # Menggabungkan newDict ke myDict

print(myDict)                           # Output: {'name': 'Edy', 'age': 26, 'a': 1, 'b': 2, 'c': 3}