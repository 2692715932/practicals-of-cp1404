from prac06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("visual_basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    programming_languages = [ruby, python, visual_basic, java, c_plus_plus]
    print(ruby)
    print(python)
    print(visual_basic)
    print(java)
    print(c_plus_plus)
    print("The dynamically typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name_of_language)


if __name__ == '__main__':
    main()
