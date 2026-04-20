myDict = {'name': 'Edy', 'age': 26}   # Dictionary awal

print(myDict.setdefault('name', 'added'))   # Key 'name' sudah ada → tidak berubah → Output: Edy
print(myDict)                               # Output: {'name': 'Edy', 'age': 26}

print(myDict.setdefault('name1', 'added'))  # 'name1' belum ada → ditambahkan → Output: added
print(myDict)                               # Output: {'name': 'Edy', 'age': 26, 'name1': 'added'}

print(myDict.pop('name1', 'not'))           # Menghapus 'name1' → Output: added
print(myDict)                               # Output: {'name': 'Edy', 'age': 26}