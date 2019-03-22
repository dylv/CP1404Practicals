"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def find_score(score):
    if score < 0:
        return "Invalid Score"
    elif score > 100:
        return "Invalid Score"
    elif 90 > score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    print(find_score(score))


main()