from collections import deque


def solution(n, k):
    people = deque([i + 1 for i in range(n)])
    # OR deque(range(1, n+1)) 로도 가능
    key = 0

    for i in range(n - 1):
        for _ in range(k - 1):
            person = people.popleft()
            people.append(person)
        people.popleft()

    winner = people.popleft()

    return winner


if __name__ == "__main__":
    answer1 = solution(5, 2)
    print(answer1)
