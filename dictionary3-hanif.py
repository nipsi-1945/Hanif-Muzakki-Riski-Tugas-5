myDict = {'name': 'Edy', 'age': 26}   # Membuat dictionary
myDict['address'] = 'London'          # Menambah data
myDict['age'] = 27                    # Update data

def traverseDict(data):               # Fungsi traverse
    for key in data:
        print(key, data[key])

traverseDict(myDict)                  # Baru dipanggil


#output name Edy age 27 address London