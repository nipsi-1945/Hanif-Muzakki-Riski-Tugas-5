myDict = {'name': 'Edy', 'age': 26}   # Dictionary awal

print(myDict.get('name', 26))   # Ambil value 'name' → Output: Edy
print(myDict.get('city', 27))   # 'city' tidak ada → pakai default 27 → Output: 27
print(myDict.get('city'))       # 'city' tidak ada → default None → Output: None