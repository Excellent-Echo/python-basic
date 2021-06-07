single_str = 'helo "ola" helo'
double_str = "helo 'ola' helo"

backslash_str = 'have a g\'day'
bs_str = "have a g\"day"

# print(backslash_str)

path = 'C:\\Users\\Member\\MYPROJECT'

enter_str = 'helo \t helo \t helo'

# print(enter_str)

# print(path)

#  ======================================
# penggabungan string

str1 = "string"
str2 = "this is " + str1
# print(str2)

# versi 3.6
str1 = "string"
str2 = f"this is {str1}"


str1 = "string"
str2 = "this is %s" % str1
# print(str2)

# ==============================
# fungsi string

str = "this is string"

# print(len(str))

# print(str[1])

# print(str.upper())

# print(str.capitalize())

slice_str = str[5:]

print(slice_str)