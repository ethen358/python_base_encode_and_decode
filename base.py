# Decode or Encode program
# Created by ethen358
import base64
# 1. Variables
encode = "encode"
Encode = "encode"
ENCODE = "encode"
decode = "decode"
Decode = "decode"
DECODE = "decode"
b64 = "b64"
b32 = "b32"
b16 = "b16"


# 2. Questions
print("Would you like to encode or decode this string")
e_or_d = input()
print("")
print("")
print("Which format will you be using")
print("b64, b32, or b16?")
form = input()
print("")
print("")
print("How many times would you like to do this?")
count = input()
print("")
print("")
print("Please enter the string surrounded by \"Double Quotes\":")
string = input()
print("")
print("")

# 2. Program
def base(e_or_d, form, count, string):
    if e_or_d == "encode":
        count = count
        a = 0
        while count > a and form == "b64":
            return base64.b64encode(string)
            a += 1



    #elif e_or_d == "decode":


    else:
        return "Please choose encode or decode."


print(e_or_d)
print(form)
print(count)
print(string)