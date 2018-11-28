# def check_NESW(current_pos, board, next_char, word):
#     adjustments = [[-1,0],[0,1],[1,0],[0,-1]]
#     for i in adjustments:
#         next_pos = [current_pos[0]+i[0], current_pos[1]+i[1]]
#         print next_pos
#         if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] > len(board) or next_pos[1] > len(board[1]):
#             pass
#         elif board[next_pos[0]][next_pos[1]] == next_char:
#             print next_char, next_pos
#
#
#
# def word_search(board, word):
#     word_index = 0
#     for i, row in enumerate(board):
#         for j, ch in enumerate(row):
#             if ch == word[word_index]:
#                 check_NESW([i, j], board, word[word_index + 1], word)
#
# def main():
#     print word_search([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCCED")
#     print word_search([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "SEE")
#     print word_search([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCB")
#
# if __name__ == '__main__':
#     main()
