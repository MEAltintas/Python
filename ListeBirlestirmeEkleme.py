liste = [2, 5, 7, 8, 3, 5, 8, 2]
liste.append(3)  #listenin sonuna ekleme
print(liste)
print()
liste2 = liste + [3, 7]
print(liste2)
liste2.append(99)
print(liste2)
print()

# Listenin belli bir yerine eleman ekleme insert() komutu ile yapılır.
liste2.insert(3, 50)
print(liste2)