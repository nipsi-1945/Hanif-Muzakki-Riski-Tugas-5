# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}  # Membuat dictionary

print(sorted(myDict, key=len))  # Mengurutkan key → ['aas', 'udd', 'sseo', 'werwi', 'eooooa']

print(myDict)                   # Dictionary asli → {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

myDict.clear()                  # Menghapus semua isi dictionary

print(myDict)                   # Output: {} (kosong)