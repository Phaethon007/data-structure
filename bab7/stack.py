top=0
mymax=eval(input("Masukkan jumlah maksimum stack:"))
def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def Push(stack,item):
    stack.append(item)
    print("--Memasukkan",item,"ke stack--")
def Pop(stack):
    if isEmpty(stack):
        return ("**Maaf,stack sudah kosong**")
    return stack.pop()
stack=createStack()
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Tampilkan")
    print("4.Keluar")
    ch=int(input("Masukkan pilihan:"))
    if ch==1:
        if top<mymax:
            item=input("Masukkan stack sembarang:")
            Push(stack,item)
            top+=1
        else:
            print("**Stack sudah Penuh**")
    elif ch==2:
        print(Pop(stack))
    elif ch==3:
        print(stack)
    else:
        print("Keluar..Sampai jumpa lagi...")
        break