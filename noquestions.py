import base64

e_or_d = ""
form = "b64"
count = 5
#actual = 0
message = "Will this work?"

def encoder64(form, message, count):
    count = count
    actual = 0
    print(count)
    while actual < count:
        message = message
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("ascii")
        return base64_message
        actual +=1



print(encoder64(form, message, count))