def toStr (n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
n = int(input("Masukkan bilangan integer: "))
base = int(input("Masukkan bilangan (2 atau 16):"))
print("Hasil konversi bilangan ",n," dengan basis",base,"adalah:",toStr(n,base))