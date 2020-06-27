# Decode or Encode program
# Created by ethen358
import base64
# 1. Variables
#e = "encode"
#encode = "encode"
#Encode = "encode"
#ENCODE = "encode"
#d = "decode"
#decode = "decode"
#Decode = "decode"
#DECODE = "decode"
#b64 = "b64"
#b32 = "b32"
#b16 = "b16"


# 2. Questions
print("Would you like to encode or decode this string?")
e_or_d = input(str())
print("")
print("")
print("Which format will you be using:")
print("b64, b32, or b16?")
form = input(str())
print("")
print("")
print("How many times would you like to do this?")
count = input()
count = int(count)
print("")
print("")
print("Please enter the string surrounded by \"Double Quotes\":")
message = input(str())
print("")
print("")

# 2. Program
def encoder64(message, count):
    lst = range(count)
    for i in lst:
        print("")
        print(int(i)+1)
        if i < count:
            message = message
            message_bytes = message.encode("ascii")
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode("ascii")
            message = base64_message
            print(base64_message)

def encoder32(message, count):
    lst = range(count)
    for i in lst:
        print("")
        print(int(i)+1)
        if i < count:
            message = message
            message_bytes = message.encode("ascii")
            base32_bytes = base64.b32encode(message_bytes)
            base32_message = base32_bytes.decode("ascii")
            message = base32_message
            print(message)

def encoder16(message, count):
    lst = range(count)
    for i in lst:
        print("")
        print(int(i)+1)
        if i < count:
            message = message
            message_bytes = message.encode("ascii")
            base16_bytes = base64.b16encode(message_bytes)
            base16_message = base16_bytes.decode("ascii")
            message = base16_message
            print(message)

def decoder64(message, count):
    lst = range(int(count))
    for i in lst:
        print("")
        print(int(i)+1)
        if i < count:
            message = message
            base64_bytes = message.encode("ascii")
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode("ascii")
            print(message)
    
def decoder32(message, count):
    lst = range(count)
    for i in lst:
        print("")
        print(int(i)+1)
        if i < count:
            message = message
            base32_bytes = message.encode("ascii")
            message_bytes = base64.b32decode(base32_bytes)
            message = message_bytes.decode("ascii")
            print(message)

def decoder16(message, count):
    lst = range(count)
    for i in lst:
        print("")
        print(int(i)+1)
        if i < count:
            message = message
            base16_bytes = message.encode("ascii")
            message_bytes = base64.b16decode(base16_bytes)
            message = message_bytes.decode("ascii")
            print(message)
#encoder64(message, count)
#decoder64(message, count)
#encoder32(message, count)
#decoder32(message, count)
#encoder16(message, count)
#decoder16(message, count)


# 3. Encoder
def e_vs_d(e_or_d, message, count):
    if e_or_d == "encode" and form == "b64":
        encoder64(message, count)
        #elif form == "b32"

        #elif form == "b16"

        #else:
            #print("The options were: b64, b32, b16")
    #elif e_or_d == "decode"

    else:
        print("Pick encode or Decode")

e_vs_d(e_or_d, message, count)














