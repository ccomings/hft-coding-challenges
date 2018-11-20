fun longestSub(str: String): Int {
    var maxLen = 0
    var currLen = 0
    var currSet: MutableSet<Char> = mutableSetOf()

    for (char in str) {
        currSet.add(char)
        currLen += 1
        if (currSet.size < currLen) {
            currSet = mutableSetOf()
            currLen = 0
        }
        maxLen = Math.max(maxLen, currLen)
    }
    return maxLen
}

fun main(args: Array<String>) {
    println(longestSub("abcabcbb")) // 3
    println(longestSub("bbbbb"))  // 1
    println(longestSub("pwwkew"))  // 3
}