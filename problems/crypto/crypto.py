def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    len_alphabet = ord("Z") - ord("A") + 1

    for char in text:
        if char.isupper():
            print((ord(char) + shift - ord("A")) % len_alphabet + ord("A"))
            result += chr((ord(char) + shift - ord("A")) % len_alphabet + ord("A"))
        elif char.islower():
            result += chr((ord(char) + shift - ord("a")) % len_alphabet + ord("a"))
        else:
            result += char
    return result
