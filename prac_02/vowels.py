def get_vowels(string):
    count = 0
    for letter in string:
        if letter.islower() in "aeiou":
            count += 1
            return count


user_word = str(input("Enter word: "))
num_vowels = get_vowels(user_word)
print("The number of vowels in your word is {}".format(num_vowels))
