def solution(n):
    answer = 0
    board = [0 for i in range(n)]

    def Queen(count):
        nonlocal answer
        if count == n:
            answer += 1
            return
        else:
            for x in range(n):
                board[count] = x
                for y in range(count):
                    if board[y] == x or abs((x-board[y])/(count-y)) == 1:
                        break
                else: 
                    Queen(count+1)
    Queen(0)
    return answer