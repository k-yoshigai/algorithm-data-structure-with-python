from typing import List

NUM_ALPHABET_MAPPPING = {
    0: "+",
    1: "@",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}


def phone_mnemonic_recursive(phone_number: str) -> List[str]:
    phone_number_digits = [int(s) for s in phone_number.replace("-", "")]

    candidate = []
    # To prevent index out of range error when assigning char to tmp
    # in the find_candidate_alphabet function.
    tmp = [""] * len(phone_number_digits)

    def find_candidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number_digits):
            candidate.append("".join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPPING[phone_number_digits[digit]]:
                # tmp is not appended.
                # So you don't need to worry removing the value for the next time.
                tmp[digit] = char

                # Just Passing digit + 1 to find_candidate_alphabet,
                # but not updating it, like digit += 1.
                find_candidate_alphabet(digit + 1)

    find_candidate_alphabet()
    return candidate


def phone_mnemonic_stack(phone_number: str) -> List[str]:
    phone_number_digits = [int(s) for s in phone_number.replace("-", "")]

    candidate = []
    # Prevent indexError when calling pop() for the first time,
    # and for the first while loop.
    stack = [""]

    while len(stack) != 0:
        alphabets = stack.pop()

        if len(alphabets) == len(phone_number_digits):
            candidate.append(alphabets)
        else:
            for char in NUM_ALPHABET_MAPPPING[phone_number_digits[len(alphabets)]]:
                stack.append(alphabets + char)

    return candidate


if __name__ == "__main__":
    print("LOVEPYTHON" in phone_mnemonic_recursive("568-379-8466"))
    print("LOVEPYTHON" in phone_mnemonic_stack("568-379-8466"))
