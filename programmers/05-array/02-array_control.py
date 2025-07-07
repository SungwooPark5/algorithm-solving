def solution(array: list):
    answer = set(array)

    answer = list(answer)

    # Arrays.sort()는 return값이 None임
    # 따라서 재할당하지 말고 호출만 해야 됨
    answer.sort(reverse=True)

    return answer


def test_solution():

    answer = solution([3, 3, 1, 2])

    if answer == [3, 2, 1]:
        pass
    else:
        print("Wrong!")
        print(f"answer: {answer}")
        return

    print("All test passed!")


if __name__ == "__main__":
    test_solution()
