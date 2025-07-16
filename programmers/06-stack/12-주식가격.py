def solution(prices):
    answer = [0]*len(prices)
    stack=[]
    
    for i, price in enumerate(prices):
        if len(stack)!=0:
            while price<prices[stack[-1]]:
                index = stack.pop()
                length = i-index
                answer[index]=length
                
                if len(stack)==0:
                    break
                
        stack.append(i)
        
    while len(stack)!=0:
        index = stack.pop()
        length = len(prices)-1-index
        answer[index]=length
        
    return answer