# 트리 구조를 생각하여 풀기
# (a+1)//2를 통해 부모 노드를 계산할 수 있음
# 계산한 부모 노드가 같을 경우, 서로 같은 경기에 들어왔다고 할 수 있음
def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer
