def solution(s):
    answer = -1
    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            # pop하는 대신 stack[-1]로 확인하는 방법도 있음
            # 어차피 실제 스택은 아니니 인덱싱하는 것도 좋을 듯
            c1 = stack.pop()
            if c1 == c:
                continue
            else:
                stack.append(c1)
                stack.append(c)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer
