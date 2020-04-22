"""
CP1404/CP5632 Practical - Suggested Solution
A program to count the occurrences of words in a string
"""
WORDS = {}


def main():
    text_of_user = str(input("Enter a text what you like: "))
    for word in text_of_user.strip().split(' '):
        if word in WORDS:
            WORDS[word] += 1
        else:
            WORDS[word] = 1
    max_word_length = max([len(key) for key in WORDS.keys()])
    NEW_WORDS = sorted(WORDS.keys())
    for key in NEW_WORDS:
        print("{:{}} : {}".format(key, max_word_length, WORDS[key]))


if __name__ == '__main__':
    main()