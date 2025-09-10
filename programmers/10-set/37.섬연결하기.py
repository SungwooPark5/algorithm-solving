"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42861#

섬 연결에 필요한 비용이 주어졌을 때, 모든 섬을 연결하는 최소 비용을 구하는 문제
"""


# 기본적으로 크루스칼 알고리즘을 사용한다.
# 이 과정에서 union-find 알고리즘을 사용하여 사이클이 발생하는지 확인한다.
# 시간 복잡도는 O(E log E) (E는 간선의 개수): 간선 정렬에 가장 큰 시간 소요
# union by rank를 이용하여 find 연산의 시간 복잡도를 줄일 수 있다.
def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    sorted_costs = sorted(costs, key=lambda x: x[2])

    def find_root(i):
        if parents[i] != i:
            parents[i] = find_root(parents[i])
        return parents[i]

    for node1, node2, cost in sorted_costs:
        if find_root(node1) != find_root(node2):
            parents[find_root(node2)] = find_root(node1)
            answer += cost

    return answer
