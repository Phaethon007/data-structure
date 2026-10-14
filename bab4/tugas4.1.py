def baca_file_pegawai(nama_file):
    data = []
    with open(nama_file, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            if line.strip():
                nama, gaji = line.strip().split(",")
                data.append({"nama": nama, "gaji": int(gaji)})
    return data

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["gaji"] < key["gaji"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j]["gaji"] > arr[max_idx]["gaji"]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

data_pegawai = baca_file_pegawai("bab4/data_pegawai.txt")

print("=== HASIL INSERTION SORT (25 PEGAWAI) ===")
res_insertion = insertion_sort(list(data_pegawai))
for idx in range(1, 26):
    p = res_insertion[idx - 1]
    print(f"{idx}. {p['nama']}: Rp {p['gaji']:,}")

print("\n=== HASIL SELECTION SORT (25 PEGAWAI) ===")
res_selection = selection_sort(list(data_pegawai))
for idx in range(1, 26):
    p = res_selection[idx - 1]
    print(f"{idx}. {p['nama']}: Rp {p['gaji']:,}")
