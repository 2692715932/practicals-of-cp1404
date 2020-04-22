"""
CP1404/CP5632 Practical - Suggested Solution
A program that allows user to look up hexadecimal colour codes like those at http://www.color-hex.com/color-names.html
"""

NAME_TO_CODE = {"ALICEBlUE": "#f0f8ff",
                "ANTIQUEWHITE": "#faebd7",
                "BEIGE": "#f5f5dc",
                "BLACK": "#000000",
                "BLANCHEDALMOND": "#ffebcd",
                "BLUEVIOLET": "#8a2be2",
                "BROWN": "#a52a2a",
                "BURLYWOOD": "#deb887",
                "CADETBLUE": "#5f9ea0",
                "CHOCOLATE": "#d2691e",
                "CORAL": "#ff7f50",
                "CORNFLOWERBLUE": "#6495ed",
                "DARKGOLDENROD": "#b8860b",
                "DARKGREEN": "#006400"}
print(NAME_TO_CODE)


def main():
    """main()_method - starting point of the program"""
    color_name = input("Enter the name of color: ").strip().upper()  # strip white spaces. lowercase inputs also work
    max_key_length = max([len(key) for key in NAME_TO_CODE.keys()])
    while color_name != "":
        if color_name in NAME_TO_CODE:
            print("{:{}} is {}".format(color_name, max_key_length, NAME_TO_CODE[color_name],))
        else:
            print("Invalid color name")
        color_name = input("Enter the name of color: ").strip().upper()


if __name__ == '__main__':
    main()