# jika import nama fungsi/nama file aja maka saat dipanggil perlu dipanggel dengan nama fungsi/nama file.nama method
import function

hello = function.say_hello("Eko")
print(hello)

hasil = function.total(1,2,3)
print(hasil)

# jika ingin memnaggil dengan nama method aja tanpa disertai fungsi maka 
# diimport dengan sebagai berikut
from function import say_hello
from function import total

hello = say_hello("Budi")
print(hello)

hasil = total(1,2,3, 5)
print(hasil)