import pandas as pd
import os
def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]

    kiri = []
    tengah = []
    kanan = []

    for angka in data:
        if angka < pivot:
            kiri.append(angka)
        elif angka > pivot:
            kanan.append(angka)
        else:
            tengah.append(angka)

    return quick_sort(kiri) + tengah + quick_sort(kanan)

file = r"C:\coding\Struktur Data\bab5\AngkaRandom.xlsx"

df = pd.read_excel(file, header=None)

data = pd.to_numeric(
    df.iloc[:, 0], errors="coerce"
).dropna().tolist()

hasil = quick_sort(data)

print("=== DATA SEBELUM SORTING ===")
print(data)

print("\n=== DATA SESUDAH SORTING ===")
print(hasil)

print("\nJumlah data sebelum sorting:", len(data))
print("Jumlah data sesudah sorting:", len(hasil))
print("Berhasil diurutkan:", hasil == sorted(data))

hasil_file = os.path.join(
    os.path.dirname(file),
    "Hasil_QuickSort.xlsx"
)

with pd.ExcelWriter(hasil_file, engine="openpyxl") as writer:
    pd.DataFrame({
        "Data Sebelum Sorting": pd.Series(data)
    }).to_excel(
        writer, sheet_name="Sebelum Sorting", index=False
    )

    pd.DataFrame({
        "Data Sesudah Sorting": pd.Series(hasil)
    }).to_excel(
        writer, sheet_name="Sesudah Sorting", index=False
    )

print("\nFile hasil berhasil disimpan:")
print(hasil_file)
