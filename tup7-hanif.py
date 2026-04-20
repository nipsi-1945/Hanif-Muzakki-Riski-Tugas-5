newTuple = ('a', 'b', 'c', 'd', 'e')   # Tuple

def searchInTuple(pTuple, element):    # Fungsi mencari elemen dalam tuple
    for i in pTuple:                  # Loop setiap elemen
        if i == element:              # Cek apakah sama dengan yang dicari
            return pTuple.index(i)    # Kembalikan index elemen
    return 'The element does not exist'  # Jika tidak ditemukan

print(searchInTuple(newTuple, 'c'))   # Output: 2