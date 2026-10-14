def baca_file_mahasiswa(nama_file):
    data = []
    with open(nama_file, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            if line.strip():
                nama, bd, so, sd = line.strip().split(",")
                data.append({
                    "nama": nama,
                    "Basis Data": int(bd),
                    "Sistem Operasi": int(so),
                    "Struktur Data": int(sd)
                })
    return data

def bubble_sort(arr, matkul):
    n = len(arr)
    arr_copy = list(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j][matkul] < arr_copy[j + 1][matkul]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

data_mahasiswa = baca_file_mahasiswa("bab4/data_mahasiswa.txt")
mata_kuliah = ["Basis Data", "Sistem Operasi", "Struktur Data"]

if len(data_mahasiswa) < 5:
    print(f"Eror: Jumlah data di file hanya {len(data_mahasiswa)}. Minimal harus ada 5 data mahasiswa!")
else:
    for matkul in mata_kuliah:
        print(f"\n> Top 5 Mahasiswa Terbaik - {matkul}:")
        res_sorted = bubble_sort(data_mahasiswa, matkul)
        for rank in range(1, 6):
            m = res_sorted[rank - 1]
            print(f"Rank {rank}: {m['nama']} ({m[matkul]})")
