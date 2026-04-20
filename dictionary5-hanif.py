myDict = {'name': 'Edy', 'age': 26}     # Membuat dictionary
myDict['address'] = 'London'            # Menambahkan address
myDict['age'] = 27                      # Mengubah age jadi 27

# Delete atau remove data
myDict.pop('name')                      # Menghapus key 'name'

print(myDict)                           # Output: {'age': 27, 'address': 'London'}