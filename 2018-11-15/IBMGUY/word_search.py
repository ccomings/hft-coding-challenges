class Solution(object):
    def exist(self, board, word):
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                letter = board[row_idx][col_idx]
                if letter == word[0]:
                    if search_from_index(row_idx, col_idx, board, word) == True:
                        return True
        return False

def search_from_index(y, x, board, word, seen_indices = []):
    try:
        if len(word) == 0:
            return True

        if [y, x] in seen_indices:
            return False

        if board[y][x] == word[0]:
            seen_indices.append([y, x])
            return (
                    search_from_index(y, x+1, board, word[1:], seen_indices)
                    or search_from_index(y+1, x, board, word[1:], seen_indices)
                    or search_from_index(y-1, x, board, word[1:], seen_indices)
                    or search_from_index(y, x-1, board, word[1:], seen_indices)
             )
        else:
            return False
    except IndexError:
        return False


# edge testcases
# [["a","a"]], "aaa"
# [["a"]], "a"
