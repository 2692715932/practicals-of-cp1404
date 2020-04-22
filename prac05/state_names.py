"""
CP1404/CP5632 Practical - Suggested Solution
State names in a dictionary
File has been reformatted and state inputs can be any case
"""

STATE_NAMES = {"QLD": "Queensland",
               "NSW": "New South Wales",
               "NT": "Northern Territory",
               "WA": "Western Australia",
               "ACT": "Australian Capital Territory",
               "VIC": "Victoria",
               "TAS": "Tasmania"}
print(STATE_NAMES)


def main():
    state_short_name = input("Enter short state: ").strip().upper()  # strip white spaces. lowercase inputs also work

    while state_short_name != "":
        if state_short_name in STATE_NAMES:
            print("{:3} is {}".format(state_short_name, STATE_NAMES[state_short_name]))
        else:
            print("Invalid short state")
        state_short_name = input("Enter short state: ").strip().upper()


if __name__ == '__main__':
    main()