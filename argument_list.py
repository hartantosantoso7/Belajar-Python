def jumlahkan(*list_angka):
    total = 0
    for data in list_angka:
        total = total + data
    print(f"Total {list_angka} = {total}")

jumlahkan(10, 10)