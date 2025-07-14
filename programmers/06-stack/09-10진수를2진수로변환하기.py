def solution(num):
    answer = []

    while num != 0:
        answer.append(str(num % 2))
        num = num // 2

    answer.reverse()
    answer = "".join(answer)

    print(answer)
    return answer


def test_solution():
    solution(10)
    assert solution(10) == "1010"
    assert solution(27) == "11011"
    assert solution(12345) == "11000000111001"


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
