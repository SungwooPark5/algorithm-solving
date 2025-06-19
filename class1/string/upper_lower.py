user_input = input()

string_list = list(user_input)

for c in string_list:

    if c == c.upper():
        print(c.lower(), end="")
    else:
        print(c.upper(), end="")
