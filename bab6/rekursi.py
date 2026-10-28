def listsum(numList):
    if len (numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

print ("Masukkan list data:  ")
numList = [int(x) for x in input().split()]
print ("Hasil Penjumlahan:",listsum(numList))