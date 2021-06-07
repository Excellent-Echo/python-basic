import math


# selain + - / * %
# kita bisa menggunakan ** untuk pangkat

x = 4

# print(x**3)

# penggunaan and dan or
condition1 = 10 > 5
condition2 = 5 < 1

# kita tidak menggunakan && tapi menggunakan and
# kita tidak menggunakan || tapi menggunakan or

# print(condition1 or condition2) 

# math module

x = 8.2131231232

# print(math.floor(x))
# print(math.ceil(x))

# print(math.sqrt(16))

# ==================================
# tipe data list

# data_list = ["1", 2, False, 3.14]

data_list = ["1", "1","1","1","1","1"]
# print(data_list)
# urutan index 0,1,2,3,4,5,6, ...
# urutan index list dari belakang, -1,-2,-3, ... 


# print(data_list)

# print(data_list[1:3])
# func list func / function => def

# print(len(data_list))

# print(data_list[4])

# print(data_list[-1]) # mengganti index terakhir

# append
data_list.append("helo") # cuma bisa diisi satu data / value ke list
# print(data_list)

# insert
data_list.insert(-1, "1")
# print(data_list)

#pop

# data_list.pop(-1)
# print(data_list)

# remove

data_list.remove("1") # cuma menghapus sekali karakter yang ditemukan,
# data_list.remove("1")
# data_list.remove("1")
# data_list.remove("1")
# print(data_list)

# ============================================
# tuple

data_tuple = ("afista", "pratama")

# print(data_tuple[1])

# ============================================
# dictionary

data_dict = {
    "name" : "afista",
    "age" : 23,
    "hobbies" : ["coding", "sleeping", "mancing"]
}


# print(data_dict)

data_dict["address"] = "jember"
data_dict["name"] = "jaya"

print(data_dict["name"])
print(data_dict.get("name"))

data_dict.pop("age")

print(data_dict)