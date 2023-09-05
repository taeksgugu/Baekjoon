board = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
         [10, 13, 16, 19],
         [20, 22, 24],
         [30, 28, 27, 26],
         [25, 30, 35],
         [40, 0]]
result = 0

dice_list = list(map(int, input().split()))


def game_start(horses, dice_idx, acc):
    global result

    if dice_idx == 10:
        result = max(result, acc)
        return
    
    loop = horses.index([0, 0]) + 1 if [0, 0] in horses else 4
    
    for idx, loc in enumerate(horses):
        if idx >= loop:
            break
        
        new_loc = [loc[0], loc[1] + dice_list[dice_idx]]

        if new_loc == [0, 5]: new_loc = [1, 0]
        elif new_loc == [0, 10]: new_loc = [2,0]
        elif new_loc == [0, 15]: new_loc = [3, 0]
        else:
            while new_loc[1] >= len(board[new_loc[0]]):
                if new_loc[0] in [0, 4]:
                    new_loc[1] -= len(board[new_loc[0]])
                    new_loc[0] = 5

                elif 1 <= new_loc[0] <= 3:
                    new_loc[1] -= len(board[new_loc[0]])
                    new_loc[0] = 4

                else:
                    new_loc[1] = 1

        if new_loc != [5, 1] and new_loc in horses:
            continue

        game_start(horses[:idx] + [new_loc] + horses[idx + 1:], dice_idx + 1, acc + board[new_loc[0]][new_loc[1]])


game_start([[0, 0] for _ in range(4)], 0, 0)

print(result)
