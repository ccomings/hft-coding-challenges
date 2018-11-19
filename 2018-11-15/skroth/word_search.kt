fun getOptions(board: List<List<Char>>, pos: Pair<Int, Int>): List<Pair<Int, Int>> {
    return listOf(
        Pair(pos.first - 1, pos.second),
        Pair(pos.first, pos.second - 1),
        Pair(pos.first, pos.second + 1),
        Pair(pos.first + 1, pos.second)
    ).filter {it.first in board.indices && it.second in board[it.first].indices}
}

fun wordSearch(board: List<List<Char>>, word: String): Boolean {
    if (word.isEmpty()) {
        return true
    }
    if (board.isEmpty()) {
        throw IllegalArgumentException("The board should not be empty")
    }
    if (!board.all {it.size == board[0].size}) {
       throw IllegalArgumentException("The board should be rectangular")
    }

    // keep track of where letters exist
    val charToLoc: HashMap<Char, MutableList<Pair<Int, Int>>> = hashMapOf()
    for ((i, row) in board.withIndex()) {
        for ((j, char) in row.withIndex()) {
            if (char in charToLoc) {
                charToLoc[char]?.add(Pair(i, j))
            } else {
                charToLoc[char] = mutableListOf(Pair(i, j))
            }
        }
    }
    val starts = charToLoc[word[0]]
    var foundWord = false

    if (starts == null) {
        return false
    }

    val start = starts.last()
    starts.removeAt(starts.size - 1)
    var currPath = mutableListOf(start)
    var visited = mutableSetOf(start)
    val leads: MutableList<MutableList<Pair<Int, Int>>> = starts.map {mutableListOf(it)}.toMutableList()
    println(leads)

    while (visited.size < word.length || leads.size > 0) {
        val currPos = currPath.last()
        var options: List<Pair<Int, Int>> = listOf()
        visited.add(currPos)

        if (currPath.size < word.length) {
            options = getOptions(board, currPos).filter {
                !visited.contains(it) && board[it.first][it.second] == word[currPath.size]
            }
        }

        val currString = currPath.map {board[it.first][it.second]}.joinToString("")
        println(currString)
        if (currString == word) {
            foundWord = true
            break
        }
        if (options.isEmpty()) {
            if (leads.isEmpty()) {
                break
            }
            currPath = leads.last()
            visited = currPath.toMutableSet()
            leads.removeAt(leads.size - 1)
        } else {
            for (optionPair in options.subList(0, options.size - 1)) {
                leads.add((currPath + mutableListOf(optionPair)) as MutableList<Pair<Int, Int>>)
            }
            currPath.add(options.last())
        }
    }
    return foundWord
}

fun main(args: Array<String>) {
    val board: List<List<Char>> = listOf(
        listOf('A', 'B', 'C', 'A'),
        listOf('S', 'F', 'C', 'S'),
        listOf('A', 'D', 'E', 'E')
    )
    println(wordSearch(board, "ABCCED"))
    println(wordSearch(board, "SEE"))
    println(wordSearch(board, "ABCB"))
}