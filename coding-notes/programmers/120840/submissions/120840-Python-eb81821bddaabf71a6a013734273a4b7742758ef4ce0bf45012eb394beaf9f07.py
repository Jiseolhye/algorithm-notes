def solution(balls, share):
    answer = 1
    
    for i in range(balls, balls - share, -1):
        answer *= i
    
    for j in range(share, 1, -1):
        answer //= j
        
    return answer