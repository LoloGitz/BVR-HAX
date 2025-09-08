letters = "abcdefghijklmnopqrstuvwxyz"

def encrypt(input: str, offset: int, type: str) -> str:
    input = input.lower()
    result = ""

    for i in input:
        if i in letters:
            i = letters[letters.index(i) + offset % 26]
        
        result += i

    return result

def decrypt(input:str, offset: int) -> str:
    return encrypt(input, -offset)

message = input("what do you want to encrypt?")

enc = encrypt(message, 1, "encrypt")
print(enc)

dec = decrypt(enc, 1, "decrypt")
print(dec)