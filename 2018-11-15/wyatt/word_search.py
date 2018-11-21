# -*- coding: utf-8 -*-


def word_search(board, word):
    """ Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are those
    horizontally or vertically neighboring. The same letter cell may not be used more than once in one word string.
    Your function should take a board and a word as input and return true or false. """
    width = len(board[0])
    height = len(board)

    def search_helper(word_part, y, x, seen):
        """ Recursive search function called once initial character found. """
        to_check = []
        if (y - 1) >= 0 and ((y - 1), x) not in seen:
            to_check.append((y - 1, x))
        if (y + 1) < height and ((y + 1), x) not in seen:
            to_check.append((y + 1, x))
        if (x - 1) >= 0 and (y, (x - 1)) not in seen:
            to_check.append((y, (x - 1)))
        if (x + 1) < width and (y, (x + 1)) not in seen:
            to_check.append((y, (x + 1)))

        for j, i in to_check:
            first_char = word_part[0]
            if first_char == board[j][i]:
                if len(word_part) == 1:
                    return True
                else:
                    seen.add((j, i))
                    return search_helper(word_part[1:], j, i, seen)
        return False

    found = True
    for y in xrange(height):
        for x in xrange(width):
            if word[0] == board[y][x]:
                found = found and search_helper(word[1:], y, x, {(y, x)})
    return found

if __name__ == '__main__':
    BOARD = [
        ['A', 'B', 'R', 'R'],
        ['X', 'E', 'U', 'I'],
        ['F', 'L', 'B', 'T'],
        ['I', 'X', 'X', 'O'],
        ['G', 'R', 'I', 'G']
    ]
    assert word_search(BOARD, 'FIGRIG') is True
    assert word_search(BOARD, 'ABELBURRITO') is True
    assert word_search(BOARD, 'RISIBISI') is False
