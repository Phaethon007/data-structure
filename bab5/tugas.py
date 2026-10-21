import pandas as pd
def quick_sort(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        quick_sort(data, low, pivot - 1)
        quick_sort(data, pivot + 1, high)

def partition(data, low, high):
    pivot = data[low][1]
    up = low + 1
    down = high
    done = False

    while not done:
        while up <= down and data[up][1] <= pivot:
            up += 1

        while down >= up and data[down][1] >= pivot:
            down -= 1

        if down < up:
            done = True
        else:
            data[up], data[down] = data[down], data[up]

    data[low], data[down] = data[down], data[low]
    return down

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][2].casefold() <= right[j][2].casefold():
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


df = pd.read_csv(
    "bab5/dummy_mahasiswa.txt",
    sep="|",
    dtype=str
)

df.columns = df.columns.str.strip().str.lower()
df = df.apply(lambda col: col.str.strip())

if not {"nama", "nim", "asal"}.issubset(df.columns):
    raise ValueError("Kolom harus bernama nama, nim, dan asal.")

if df[["nama", "nim", "asal"]].isna().any().any():
    raise ValueError("Data mahasiswa tidak boleh kosong.")

print("DATA MAHASISWA AWAL")
print(df.to_string(index=False))

data = df[["nama", "nim", "asal"]].values.tolist()

data_nim = [row.copy() for row in data]
quick_sort(data_nim, 0, len(data_nim) - 1)

print("\nHASIL QUICK SORT BERDASARKAN NIM")
print(pd.DataFrame(
    data_nim, columns=["Nama", "NIM", "Asal"]
).to_string(index=False))

data_asal = [row.copy() for row in data]
merge_sort(data_asal)

print("\nHASIL MERGE SORT BERDASARKAN ASAL")
print(pd.DataFrame(
    data_asal, columns=["Nama", "NIM", "Asal"]
).to_string(index=False))
