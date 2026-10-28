def f_search(a,x,n):
    f0=0
    f1=1
    f2=f0+f1
    while f2<n:
        f0=f1
        f1=f2
        f2=f0+f1
        offset=-1
    while f2>1:
        i = min(offset+f2, n-1)
        if (a[i]<x):
            f2=f1
            f1=f0
            f0=f2-f1
            offset = i
        elif (a[i]>x):
            f2=f0
            f1=f1-f2
            f0=f2-f1
        else:
            return i
    if(f1 and a [offset+1]==x):
        return offset+1
    return -1

print("Masukkan list:")
a=[int(b) for b in input().split()]
list.sort(a)
print("Data yang telah diurutkan",a)
x=eval(input("Masukkan data yang dicari:"))
n=len(a)
pos = f_search (a,x,n)
if pos >=0:
    print("Data berada pada posis",pos+1)
else:
    print("Data tidak ditemukan")