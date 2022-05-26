def c_to_j(string):
    new_words_list = list()
    words_list = list(string.split("_"))

    for i in range(len(words_list)):
        word = words_list[i]
        new_word = ""
        if i == 0:
            new_words_list.append(word)
            continue
        for j in range(len(word)):
            if j == 0:
                new_word += word[j].upper()
            else:
                new_word += word[j]
        new_words_list.append(new_word)

    return "".join(new_words_list)


def j_to_c(string):
    words_list = list()
    word = ""
    for i in range(len(string)):
        if string[i].islower():
            word += string[i]
        elif string[i].isupper():
            words_list.append(word)
            word = string[i].lower()
    words_list.append(word)
    return "_".join(words_list)


def raise_error():
    print("Error!")
    exit()


def check_error(string):
    is_c = 0
    is_j = 0
    first_upper = 0

    for i in range(len(string)):
        if string[i].isupper():
            is_j = 1
        elif string[i] == "_":
            is_c = 1

        if i != len(string) - 1:
            if string[i] == "_" and string[i + 1] == "_":
                raise_error()

    if string[0].isupper():
        first_upper = 1

    if is_c and is_j:
        raise_error()

    if is_j and first_upper:
        raise_error()

    if string[-1] == "_" or string[0] == "_":
        raise_error()

    return is_c


name = input()
is_c = check_error(name)

if is_c:
    print(c_to_j(name))
else:
    print(j_to_c(name))
