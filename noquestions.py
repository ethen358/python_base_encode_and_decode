import base64

e_or_d = ""
form = "b64"
count = 5
#actual = 0
message = ""

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
    lst = range(count)
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