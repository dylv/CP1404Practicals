from string import ascii_lowercase


def letter_count(string):
    """Count letters in string."""
    count = 0
    for char in string.lower():
        if char in ascii_lowercase:
            count += 1
    return count


user_input = str(input("Write something: "))
result = letter_count(user_input)

print(result)


