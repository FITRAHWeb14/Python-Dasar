# contoh casting tipe data

#Integer
print("===Integer===")
data_integer = 9
print("data = ", data_integer, ",type =", type(data_integer))

data_float = float(data_integer)
data_str = str(data_integer)
data_bool = bool(data_integer) #data_integer tidak boleh angka 0 akan False di data_bool
print("data = ", data_float, ",type =",type(data_float))
print("data = ",data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

# Float
print("===Float===")
data_float = 9
print("data = ", data_float, ",type =", type(data_float))

data_integer = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) #data_integer tidak boleh angka 0 akan False di data_bool
print("data = ", data_float, ",type =",type(data_float))
print("data = ",data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

#String
print("===String===")
data_str = 9
print("data = ", data_str, ",type =", type(data_str))

data_float = float(data_str)
data_integer = int(data_str)
data_bool = bool(data_str) #data_str tidak boleh angka 0 akan False di data_bool
print("data = ", data_float, ",type =",type(data_float))
print("data = ",data_integer, ",type =",type(data_integer))
print("data = ", data_bool, ",type =",type(data_bool))

#Boolean
print("===Boolean===")
data_bool = True
print("data = ", data_bool, ",type =", type(data_bool))

data_float = float(data_bool)
data_str = str(data_bool)
data_integer = int(data_integer) #data_integer tidak boleh angka 0 akan False di data_bool
print("data = ", data_float, ",type =",type(data_float))
print("data = ",data_str, ",type =",type(data_str))
print("data = ", data_integer, ",type =",type(data_integer))