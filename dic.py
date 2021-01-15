
customer = {"name":"Eko", "age":30, "address":"Subang"}

name = customer["name"]
age = customer["age"]
address = customer["address"]

# tambah data
customer["company"] = "x"

# ganti data
customer["name"] = "hartanto"

# hapus data
del customer["address"]


# for key in customer:
#     value = customer[key]
#     print(f"{key}:{value}")

# pada disctionary memiliki method yang bernamma items : data dictionary yang berupa tuple
for key, value in customer.items():
    print(f"{key}:{value}")