import java.io.File

fun part1(lines: MutableList<String>) {
    val guardNumPat = Regex("Guard #(\\d+)")
    var guardOnShift = 0  // ID of guard on current shift
    var asleepStart = 0  // Minute guard fell asleep
    val asleepMinutes = mutableMapOf<Int, MutableList<Int>>()  // Guard ID to mins they are asleep

    for (line in lines) {
        val minute = line.substring(15..16).toInt()
        when {
            line.contains("Guard #") ->
                guardOnShift = guardNumPat.find(line)?.groupValues?.get(1)?.toInt() ?: guardOnShift
            line.contains("falls asleep") -> asleepStart = minute
            line.contains("wakes up") -> {
                if (asleepMinutes.contains(guardOnShift)) {
                    asleepMinutes[guardOnShift]?.addAll(asleepStart.until(minute))
                } else {
                    asleepMinutes[guardOnShift] = asleepStart.until(minute).toMutableList()
                }
            }
        }
    }
    val sleepyGuard = asleepMinutes.keys.maxBy { asleepMinutes[it]?.size ?: 0 }
    val maxMin = asleepMinutes[sleepyGuard]?.groupBy {it} ?.maxBy {it.value.size}?.key
    if (sleepyGuard != null && maxMin != null) {
        println(sleepyGuard * maxMin)  // Answer to part1
    }
}

fun main(args: Array<String>) {
    val lines = File("inputday4.txt").useLines {it.toMutableList()}
    lines.sort()
    part1(lines)
}

