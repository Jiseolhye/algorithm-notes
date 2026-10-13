def solution(bin1, bin2):
    answer = format(int(bin1, 2) + int(bin2, 2), '0b')
    return answer