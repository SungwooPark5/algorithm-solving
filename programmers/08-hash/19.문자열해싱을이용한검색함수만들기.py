# 책의 풀이를 그대로 작성함
# def polynomial_hash(str):
#     p = 31
#     m = 1_000_000_007
#     hash_value = 0
#     for char in str:
#         hash_value = (hash_value * p + ord(char)) % m

#     return hash_value


# def solution(string_list, query_list):
#     # string_list의 각 문자열에 대해 다항 해시값을 계산
#     hash_list = [polynomial_hash(str) for str in string_list]

#     # query_list의 각 문자열이 string_list에 있는지 확인
#     result = []
#     for query in query_list:
#         query_hash = polynomial_hash(query)
#         if query_hash in hash_list:
#             result.append(True)
#         else:
#             result.append(False)

#     return False


# hash 함수를 직접 작성하지 않는 경우
def solution(string_list, query_list):
    # set은 내부 해싱을 이용함!
    string_set = set(string_list)  # O(N)
    # set에서 in 연산은 O(1)의 복잡도
    return [query in string_set for query in query_list]  # O(Q)
