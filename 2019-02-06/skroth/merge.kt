fun merge(a: MutableList<Int>, b: MutableList<Int>): MutableList<Int> {
    var i = 0
    var j = 0
    val tgtSize = a.size + b.size

    while (a.size < tgtSize) {
        if (i > a.lastIndex) {
            a.add(b[j])
            j += 1
        } else if (b[j] <= a[i]) {
            a.add(i, b[j])
            j += 1
        } else {
            i += 1
        }
    }
    return a
}

fun main(args: Array<String>) {
    val a = mutableListOf(4, 2, 23, 5, 2, 90).apply { sort() }
    val b = mutableListOf(4, 2, 9, 48, 5, 20).apply { sort() }
    println(merge(a, b))
}
