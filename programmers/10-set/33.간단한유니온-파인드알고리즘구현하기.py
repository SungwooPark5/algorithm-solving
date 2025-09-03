"""
출처: 책 356p, 문제 33

유니온-파인드 알고리즘을 구현하는 문제.
책에서는 경로 압축과 랭크도 구현하였으니 참고해보기
"""


def find(x, set_array):
    x = int(x)
    if set_array[x] == x:
        return x
    else:
        return find(set_array[x], set_array)


def union(x, y, set_array):
    x_root = find(x, set_array)
    y_root = find(y, set_array)

    if x_root != y_root:
        set_array[x_root] = y_root


def solution(k, operations):
    result = []
    set_array = [i for i in range(k)]

    for operation in operations:
        if operation[0] == "u":
            union(operation[1], operation[2], set_array)
        elif operation[0] == "f":
            if find(operation[1], set_array) == find(operation[2], set_array):
                result.append(True)
            else:
                result.append(False)

    return result


if __name__ == "__main__":
    print(solution(3, [["u", "0", "1"], ["u", "1", "2"], ["f", "0", "2"]]))
    print(
        solution(
            4, [["u", "0", "1"], ["u", "2", "3"], ["f", "0", "1"], ["f", "0", "2"]]
        )
    )
