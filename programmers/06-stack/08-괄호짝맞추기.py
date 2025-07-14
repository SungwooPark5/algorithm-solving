def solution(string):
    answer = False

    string = list(string)
    stack = []

    for c1 in string:
        print(stack)
        if len(stack) == 0:
            stack.append(c1)
        else:
            c2 = stack.pop()
            if c1 == ")" and c2 == "(":
                continue
            else:
                stack.append(c2)
                stack.append(c1)

    if len(stack) == 0:
        answer = True
    else:
        answer = False

    print(answer)

    return answer


def test_solution():
    solution("(())()")
    assert solution("(())()") == True
    assert solution("((())()") == False


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
