from typing import List

name: str = "A"
print(ord(name))  # this prints the code point of the character

try:
    byterep = name.encode(
        "ascii"
    )  # or converting the code point of the character to its byte representation
    print(byterep)  # prints a byte object
    print(bin(byterep[0]))  # prints binary representation of the byte
except UnicodeEncodeError:
    print("There was an error encoding this character")


# serialization logic

# serialization transforms structured data into bytes
# you provide some meta data for a system to use to interprete the transmitted bits
# encoding transforms or encodes text or strings in bytes

data = {"name": "Alice", "age": 25}


def functionToSerializeUserData(data: dict[str, str]) -> bytes:
    """_summary_

    Args:
        data (dict[str, str])
        Serialize user data with 'name' and 'age' into bytes.

    Each field is:
    - encoded to UTF-8

    Returns:
        bytes

    """
    try:
        arrayOfBytes: List[bytes] = []
        firstValueToEncode: str = data.get("name")
        secondValueToEncode:int = int(data.get("age"))
        print(firstValueToEncode)
        print(secondValueToEncode)
        encodedVal = firstValueToEncode.encode("utf-8")
        if type(secondValueToEncode) != int:
            print('error')
        encodedVal = encodedVal[0]
        encodedVal2 = bin(secondValueToEncode)
        print(type(encodedVal))
        print(type(encodedVal2))
        arrayOfBytes.append(bin(encodedVal))
        arrayOfBytes.append(encodedVal2)

        return arrayOfBytes
    except UnicodeEncodeError:
        raise ValueError("There was an issue encoding the structure")


print(functionToSerializeUserData(data=data))



# learning about bytes
# task: build a list of unicode code points with the string symbols
symbols = '$¢£¥€¤'
intRepr = []
hexRepr = []
binRepr = []
# base10 repr is the broker
# character -> int then if base2: int -> base2(bin) or if base16: then int -> base16(hex)
for symbol in symbols:
    intRepr.append(ord(symbol))
    hexRepr.append(hex(ord(symbol)))
    binRepr.append(bin(ord(symbol)))
    
print(intRepr)
print(hexRepr)
print(binRepr)
b = bytes(symbols.encode('utf-8'))
print(type(b))
print(b)
print(len(b))