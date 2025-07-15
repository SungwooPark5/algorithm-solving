def is_correct_string(s):
    stack = []
    is_correct = False

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            c1 = stack.pop()
            if c1 == "(" and c == ")":
                pass
            elif c1 == "{" and c == "}":
                pass
            elif c1 == "[" and c == "]":
                pass
            else:
                stack.append(c1)
                stack.append(c)

    if len(stack) == 0:
        is_correct = True
    else:
        is_correct = False

    return is_correct


def solution(s):
    answer = 0

    string_list = list(s)

    for i in range(len(s)):
        c = string_list.pop(0)
        string_list.append(c)

        if is_correct_string(string_list):
            answer += 1

    return answer
