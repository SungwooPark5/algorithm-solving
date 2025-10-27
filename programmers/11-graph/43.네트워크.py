"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/43162

네트워크가 배열로 주어질 때, 독립된 네트워크의 갯수를 구하는 문제
"""


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(n):
        visited[n] = True
        for i, connected in enumerate(computers[n]):
            if i != n and connected == 1 and not visited[i]:
                dfs(i)

    for n in range(n):
        if visited[n]:
            continue

        dfs(n)
        answer += 1

    return answer
