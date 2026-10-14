def tukar (lists,i,j):
    lists[i], lists[j] = lists[j], lists[i]
    
def bubble(listku):
    perubahan = True
    sesi = len (listku)
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j]<listku[j-1]:
                perubahan = True
                tukar(listku,j,j-1)
            j+= 1
        
        if perubahan:
            print(listku)
            
        if not perubahan:
            print("hasil akhir = %s" %str(listku))
        sesi-=1

panjangList = int(input("Panjang data yg diinginkan = "))
myList = []
for i in range(1,panjangList+1):
    angka = int (input("Masukkan data yang ke %i untuk List = " %i))
    myList.append(angka)

print("================================")
print("sebelum bubble sort")
print(myList)
print("setelah bubble sort")
bubble(myList)
