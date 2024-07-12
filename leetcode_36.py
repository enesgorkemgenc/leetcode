#LeetCode 36 - Valid Sudoku


def is_valid_sudoku(board):
    
    layers = {}

    for y in range(9):

        layers[y] = set()
        
        for x in range(9):

            num = board[y][x] 
            if num == ".":
                continue

            if num in layers[y]:
                return False
            else:
                layers[y].add(num)

            for row_check_index in range(y):
                if num in board[row_check_index][x]:
                    return False

    del layers

    for sub_box_check_index_y in range(3):
        for sub_box_check_index_x in range(3):

            box_values = set()

            for sub_box_index_y in range(3):
                for sub_box_index_x in range(3):
                    num = board[sub_box_check_index_y * 3 + sub_box_index_x][sub_box_check_index_x * 3 + sub_box_index_y]
                    
                    if num == ".":
                        continue

                    if num in box_values:
                        return False
                    else:
                        box_values.add(num)
    return True


# I don't know what to feel at this point...
