# membuat program menggunakan For-loop, List dan Range

banyak = int(input("Berapa banyak data? "))

nama = []
umur = []

for data in range(0, banyak):
    print(f"data {data}")
    print("==========================")
    input_nama = input("Nama: ")
    input_umur = int(input("Umur: "))
    print("==========================")

    nama.append(input_nama)
    umur.append(input_umur)


for n in range(0, len(nama)):
    data_nama = nama[n]
    data_umur = umur[n]
    print(f"{data_nama} berumur {data_umur} tahun")
    print("==========================")

print(nama)
print(umur)