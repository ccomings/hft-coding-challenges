from collections import defaultdict

class Solution(object):
    def exist(self, board, word):
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                letter = board[row_idx][col_idx]
                if letter == word[0]:
                    if search_from_index(row_idx, col_idx, board, word) == True:
                        return True
        return False

def search_from_index(y, x, board, word, current_index=0, seen_indices = []):
    try:
        if current_index == len(word):
            return True
        
        if [y, x] in seen_indices:
            return False

        if board[y][x] == word[current_index]:
            current_index += 1
            seen_indices.append([y, x])
            return (
                    search_from_index(y, x+1, board, word, current_index, seen_indices)
                    or search_from_index(y+1, x, board, word, current_index, seen_indices)
                    or search_from_index(y-1, x, board, word, current_index, seen_indices)
                    or search_from_index(y, x-1, board, word, current_index, seen_indices)
             )
        else:
            return False
    except IndexError:
        return False


# edge testcases
# [["a","a"]], "aaa"
# [["a"]], "a"
