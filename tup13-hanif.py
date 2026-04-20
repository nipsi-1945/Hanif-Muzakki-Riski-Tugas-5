x = 3
y = -6

x, y = (y, x)[::-1]   # Tukar nilai pakai tuple + slicing dibalik → (3, -6)
print(x, y)           # Output: 3 -6