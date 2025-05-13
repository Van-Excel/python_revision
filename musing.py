
print('"{0}" is the "{0}" of that "{1}"'.format('Vanexcel','firstname', 'ghanaian'))


import struct


payload = 'Vanexcel'
payload_byte = payload.encode("utf-8")
print(f'payload: {payload}')
print(f"payload_bytes: {payload_byte}")


payload2 = "Vanexcel"

print("Number |String | ASCII  |  UTF-8  |  BYTES")

for index, char in enumerate(payload2, start=1):
    string = char
    ascii = ord(char)
    utf8 = ord(char)
    byteHex = hex(ord(char))
    byteBinary = bin(ord(char))

    print(f"{index}  |{string} |  {ascii} |  {utf8} |  {byteHex} |  {byteBinary}")

# learning alot.
# applying my new knowledge of bytes and memory

