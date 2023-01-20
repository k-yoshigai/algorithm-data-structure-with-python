def validate_format(chars: str) -> bool:
    dictionary = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for char in chars:
        if char in dictionary.keys():
            stack.append(dictionary[char])
        if char in dictionary.values():
            if not stack or char != stack.pop():
                return False

    if stack:
        return False
    return True


if __name__ == "__main__":
    print(validate_format('{"key":"value"}'))
    print(validate_format('{"key":"value"'))
