def m_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        l_half = a[:mid]
        r_half = a[mid:]

        m_sort(l_half)
        m_sort(r_half)

        i = j = k = 0

        while i < len(l_half) and j < len(r_half):
            if l_half[i] > r_half[j]:
                a[k] = l_half[i]
                i += 1
            else:
                a[k] = r_half[j]
                j += 1
            k += 1

        while i < len(l_half):
            a[k] = l_half[i]
            i += 1
            k += 1

        while j < len(r_half):
            a[k] = r_half[j]
            j += 1
            k += 1


print("Masukkan data:")
a = [int(x) for x in input().split()]
m_sort(a)
print("Data yang telah diurutkan secara descending:", a)
