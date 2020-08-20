
matrix = [
    ['D', 'E', 'M', 'X', 'B'],
    ['A', 'O', 'E', 'P', 'E'],
    ['D', 'D', 'C', 'O', 'D'],
    ['E', 'B', 'E', 'D', 'S'],
    ['C', 'P', 'Y', 'E', 'N'],
]

# (2, 2), (1, 1), (0, 0), (0, 1)
# (2, 2), (1, 1), (2, 0), (3, 0)
# (2, 2), (1, 1), (2, 1), (1, 2)
# (2, 2), (1, 1), (2, 1), (3, 0)
# (2, 2), (1, 1), (2, 1), (3, 2)
# (2, 2), (2, 3), (2, 4), (1, 4)
# (2, 2), (2, 3), (3, 3), (3, 2)
# (2, 2), (2, 3), (3, 3), (4, 3)

def find_words(matrix, word):
    char_first = word[0]
    # print(char_first)
    
    for row in range(len(matrix)):
        # print(row)
        for col in range(len(matrix[0])):
            # print(col)
            if matrix[row][col] == char_first:
                
                helper(matrix, word, row, col, 0, [])
                print('result')
                # searching surrounding words
                
def is_valid(row, col, m, n, route):
    return  (0 <= row < m) and (0 <= col < n) and (row, col) not in route

def helper(matrix, word, row, col, index, route):
    if matrix[row][col] != word[index]:
        return
    
    if index == len(word) - 1: 
        for k in range(len(route)):
            print(word[k], route[k], end = '\t')
        print(word[len(route)], (row, col))
        print()
        return

    route.append((row, col))
    # print('*route*')
    # print(route)
    if is_valid(row - 1, col, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row - 1, col, index + 1, route)
    if is_valid(row + 1, col, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row + 1, col, index + 1, route)
    if is_valid(row, col - 1, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row, col - 1, index + 1, route ) 
    if is_valid(row, col + 1, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row, col + 1, index + 1, route)
    if is_valid(row - 1, col - 1, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row - 1, col - 1, index + 1, route)
    if is_valid(row - 1, col + 1, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row - 1, col + 1, index + 1, route)
    if is_valid(row + 1, col - 1, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row + 1, col - 1, index + 1, route) 
    if is_valid(row + 1, col + 1, len(matrix), len(matrix[0]), route):
        helper(matrix, word, row + 1, col + 1, index + 1, route)

    route.pop()
        
find_words(matrix, 'CODE')
