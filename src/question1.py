

def starts_with_b_and_ends_with_a(text: str) -> bool:
    return text.startswith("B") and text.endswith("A")


if __name__ == "__main__":
    print("BANANA starts with B and ends with A ? ", starts_with_b_and_ends_with_a("BANANA")) # True
    print("BINGO starts with B and ends with A ? ", starts_with_b_and_ends_with_a("BINGO")) # False
    print("LARANJA starts with B and ends with A ? ", starts_with_b_and_ends_with_a("LARANJA")) # False
    print("MORANGO starts with B and ends with A ? ", starts_with_b_and_ends_with_a("MORANGO")) # False
    print("'' starts with B and ends with A ? ", starts_with_b_and_ends_with_a("")) # False


