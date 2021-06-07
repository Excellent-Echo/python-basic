from ctypes import c_longlong

x = 10

variable_x = 10

# VariableX = 10
# iniVariableX = 10

data_int:int = 10
data_float:float = 3.14
data_string:str = "afista"
data_bool: bool = False

data_string = 100
# print(type(data_int)) # print tipe data
# print(data_int) # print value

data_int = 1000000000000 # angkanya berarti kita pakai int mana

data_long = c_longlong(1000000000000)

print(data_long)
print(data_int)
