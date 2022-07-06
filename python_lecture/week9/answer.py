width, height = map(int, input().split())

board = []
for i in range(width):
    board.append(list(map(int, list(input())  )    ))
print(board)

maxwidth = 0
for w in range(min(height, width) - 1, 0, -1):
    for i in range(width - w):
        for j in range(height - w):
            if board[i][j] == board[i + w][j] == board[i][j + w] == board[i + w][j + w]:
                maxwidth = w + 1
                break
            if maxwidth > 0 : break
        if maxwidth > 0 : break


if maxwidth == 0:
    maxwidth = 1

print(maxwidth * maxwidth)


