from Tablica import Tablica

tab = Tablica(5)
tab.wypelnij(20,25)
print("Tablica: ", tab)

maks = tab.maksimum()
print("Maksimum: ", maks)

min = tab.minimum()
print("Minimum: ", min)

maks2 = tab.maksimum2()
print("Maksimum2: ", maks2)

szukana = 3
index = tab.znajdz(szukana)
print("Wartość szukana: ", szukana, " Index: ", index)

    
