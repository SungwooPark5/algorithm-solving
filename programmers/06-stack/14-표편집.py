def solution(n, k, cmd):
    answer = ["O"] * n

    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]

    delete_stack = []

    k += 1

    for cmd_i in cmd:

        if cmd_i.startswith("C"):
            delete_stack.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif cmd_i.startswith("Z"):
            restore = delete_stack.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else:
            action, num = cmd_i.split(" ")
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    if len(delete_stack) != 0:
        for i in delete_stack:
            answer[i - 1] = "X"

    answer = "".join(answer)

    return answer
