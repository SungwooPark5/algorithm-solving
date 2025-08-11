# Node와 Tree(BST)를 분리하는 것이 좋을 것 같음
# BST가 Node를 포함하는 형식으로 자료구조를 만들 수 있음
# 책 301p 참고
class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)    
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)
            
    def search(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            
            return self.left.search(value)
        else:
            if self.right is None:
                return False

            return self.right.search(value)
        
        
def solution(lst, search_lst):
    answer = []
    
    tree = Tree(lst[0])
    
    for i in lst[0:]:
        tree.insert(i)
        
    for i in search_lst:
        answer.append(tree.search(i))
        
    return answer

if __name__ == "__main__":
    print(solution([5,3,8,4,2,1,7,10],[1,2,5,6]))
    print(solution([1,3,5,7,9],[2,4,6,8,10]))