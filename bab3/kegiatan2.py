def b_search(a, x, l, n):
    if l <= n:
        mid = (l + n) // 2
        if mid < len(a):
            if a[mid] == x:
                print("Data di temukan pada posisi", mid + 1)
            else:
                if a[mid] > x:
                    b_search(a, x, l, mid - 1)
                else:
                    b_search(a, x, mid + 1, n)
        else:
            print("Data tidak ditemukan")
    else:
        print("Data tidak ditemukan")

print("Masukkan list data:")
a = [int(b) for b in input().split()]
list.sort(a)
print("Urutan data adalah", a)
x = eval(input("Masukkan data yang dicari: "))
n = len(a)
b_search(a, x, 0, n - 1)
