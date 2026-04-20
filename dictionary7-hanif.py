# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}  # Membuat dictionary

print(sorted(myDict, key=len))  # Mengurutkan key berdasarkan panjang → ['aas', 'udd', 'sseo', 'werwi', 'eooooa']

print(myDict)                   # Menampilkan dictionary asli (tidak berubah) → {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}