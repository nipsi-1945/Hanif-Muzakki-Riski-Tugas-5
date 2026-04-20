myDict = {'name': 'Edy', 'age': 26}     # Membuat dictionary
myDict['address'] = 'London'            # Menambahkan address
myDict['age'] = 27                      # Mengubah age jadi 27

# Searching a dictionary
def searchDict(data, value):            # Fungsi mencari value dalam dictionary
    for key in data:                   # Loop setiap key
        if data[key] == value:         # Cek apakah value sama
            return key, value          # Jika ketemu, kembalikan key dan value
    return 'The value does not exist'  # Jika tidak ditemukan

print(searchDict(myDict, 27))          # Output: ('age', 27)