# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}  # Membuat dictionary

print(sorted(myDict, key=len))  # Mengurutkan key berdasarkan panjang huruf → Output: ['aas', 'udd', 'sseo', 'eooooa', 'werwi']