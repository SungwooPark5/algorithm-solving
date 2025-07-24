# from p234 두 개의으 수로 특정값 만들기


def solution(arr, target):
    answer = False
    hash = [0] * (target + 1)

    # 시간 복잡도: O(N^2)
    # num을 차례로 조회하는 데에 N만큼 필요하고,
    # 또 target-num이 arr에 있는지 확인하는 데에 N만큼 필요함
    # for num in arr:
    #     if (target - num) != num and (target - num) in arr:
    #         answer = True

    # 시간 복잡도: O(N) hash를 이용하는 방법
    # 해시 테이블을 먼저 만들어 조회 속도를 빠르게 함
    for num in arr:
        if num > target:
            continue
        else:
            hash[num] = 1

    for num in arr:
        if num > target:
            continue
        if (target - num) == num:
            continue
        if hash[target - num] == 1:
            answer = True
            break

    return answer


def test_solution():
    print(solution([1, 2, 3, 4, 8], 6))
    print(solution([2, 3, 5, 9], 10))


if __name__ == "__main__":
    test_solution()
