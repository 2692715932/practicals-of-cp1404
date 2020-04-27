"""
CP1404/CP5632 Practical
programming_language class
"""


class ProgrammingLanguage:

    def __init__(self, name_of_language="", typing="", reflection=False, year=0):
        self.name_of_language = name_of_language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    # which returns True/False if the programming language is dynamically typed or not
    def is_dynamic(self,):
        return self.typing.title() == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name_of_language,
                                                                           self.typing,
                                                                           self.reflection,
                                                                           self.year)


if __name__ == '__main__':
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("visual_basic", "Static", False, 1991)