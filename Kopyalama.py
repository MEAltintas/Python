liste1 = [1, 2, 3, 4, 5, 6]
liste2 = liste1
liste2[1] = 88
print(liste1)
print(liste2)

print()

liste3 = liste2.copy()
liste3[0] = 90
print(liste2)
print(liste3)