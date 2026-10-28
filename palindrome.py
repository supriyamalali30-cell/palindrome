import sys

if __name__ == "__main__":
    word = sys.argv[1]

    if word == word[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
