def solution(nodes):
    answer = []
    length = len(nodes)

    # preorder
    def travel_preorder(result, n):
        result.append(str(nodes[n - 1]))
        if (n * 2) <= length:
            travel_preorder(result, (n * 2))
        if (n * 2 + 1) <= length:
            travel_preorder(result, (n * 2 + 1))

        return result

    # inroder
    def travel_inorder(result, n):
        if (n * 2) <= length:
            travel_inorder(result, (n * 2))

        result.append(str(nodes[n - 1]))

        if (n * 2 + 1) <= length:
            travel_inorder(result, (n * 2 + 1))

        return result

    # postorder
    def travel_postorder(result, n):
        if (n * 2) <= length:
            travel_postorder(result, (n * 2))

        if (n * 2 + 1) <= length:
            travel_postorder(result, (n * 2 + 1))

        result.append(str(nodes[n - 1]))

        return result

    preorder = travel_preorder([], 1)
    inorder = travel_inorder([], 1)
    postorder = travel_postorder([], 1)

    answer.append(" ".join(preorder))
    answer.append(" ".join(inorder))
    answer.append(" ".join(postorder))

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6, 7]))
