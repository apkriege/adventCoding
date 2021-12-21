keys = []
boards = []
boardIndex = -1

file = open("./data2.txt", "r")
lines = file.readlines()

#read in file
for x, line in enumerate(lines):
    if line == "\n" :
        boards.append([])
        boardIndex += 1
    else:
        if x == 0 :
            test = line.strip('\n')
            keys = list(map(int, test.split(",")))
        else : 
            line = list(map(int,line.strip('\n').split()))
            boards[boardIndex].append(line)

#add columns to boards
for board in boards :
    lines = []
    for i, row in enumerate(board) :
        lines.append(row)

        line = []
        for j, cell in enumerate(row) :
            line.append(board[j][i])
        lines.append(line)
    board += lines


# calculates the board remaining spaces * the last index of key
def calculateBoard(keys, board, boardNum) :
    nums = []
    for rows in board :
        nums += rows

    diff = list(set(nums) - set(keys))
    score = sum(diff) * keys[-1]
    print(score)


allKeys = []
for i, key in enumerate(keys) :
    allKeys.append(key)

    for j, board in enumerate(boards) : 
        for row in board :
            if(all (x in allKeys for x in row)) :
                calculateBoard(allKeys, board, j)
                exit(0)
