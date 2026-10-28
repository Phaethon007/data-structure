front=0
rear=0
mymax=eval (input("Masukkan jumlah maksimum antrian:"))
def createQueue():
    queue=[]
    return queue
def isEmpty(queue):
    return len(queue) ==0
def enqueue(queue,item):
    queue.append(item)
    print("--Memasukkan",item,"ke antrian--")
def dequeue(queue):
    if isEmpty(queue):
        return ("**Maaf, Antrian sudah habis**")
    item=queue[0]
    del queue[0]
    return item
queue=createQueue()
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print ("4.Quit")
    ch=int(input("Masukkan pilihan:"))
    if ch==1:
        if rear<mymax:
            item=input("Masukkan antrian sembarang:")
            enqueue(queue,item)
            rear+=1
        else:
            print("**Antrian sudah penuh**")
    elif ch==2:
        print(dequeue(queue))
    elif ch==3:
        print(queue)
    else:
        print("Keluar... Sampai jumpai lagi..")
        break        