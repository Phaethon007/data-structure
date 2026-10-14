def selectionSort(alist):
    for slot in range (len(alist)-1):
        position=slot
        for location in range (len(alist)-1,slot,-1):
            if alist[location]<alist[position]:
                position = location
        
        temp = alist[slot]
        alist[slot] = alist [position]
        alist[position] = temp
alist = [54,26,93,17,77,31,44,55,20]

print("================================")
print("sebelum selection sort")
print(alist)
print("setelah selection sort")
selectionSort(alist)
print(alist)