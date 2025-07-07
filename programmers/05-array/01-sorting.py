# list.sort()의 시간 복잡도는 O(n log n)입니다.
# sort() 메소드는 Timsort 알고리즘을 사용함


def solution(arr):
    arr.sort()
    return arr


def test_solution():
    assert solution([3, 1, 2]) == [1, 2, 3]
    assert solution([5, 4, 2, 1, 3]) == [1, 2, 3, 4, 5]
    assert solution([]) == []
    assert solution([1]) == [1]


def main():
    test_solution()
    print("All tests passed!")


if __name__ == "__main__":
    main()
