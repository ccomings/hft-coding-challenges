
func lengthOfLongestSubstring(s: String) -> Int {
    if s.count < 2 {
        return s.count
    }
    // 🐇 & 🐢 represent indices in the string that run left to right
    var 🐢 = 0
    var 🐇 = 1
    // used to detect when 🐇 approaches a duplicate letter
    var lettersBeingTracked = Set<Character>() // CharacterSet is nice but not appropriate here
    // initialize longestSubstring with the first two letters in the string
    var longestSubstring = getSubstringFromIndices(s: s, start: 🐢, end: 🐇)
    // unless they are the same character
    if s[🐢] == s[🐇] {
        longestSubstring = Substring(String((s[🐇]))) // casting Character -> String -> Substring
    }

    while 🐇 < s.count {
        🐇 += 1
        var nextLetter: Character?
        if 🐇 == s.count {
            nextLetter = s[🐇 - 1]
        } else {
            nextLetter = s[🐇]
        }

        if lettersBeingTracked.contains(nextLetter!) {
            // found a duplicate, so move the turtle up past the last time the duplicate was seen
            while 🐢 < 🐇 {
                🐢 += 1
                if s[🐢 - 1] == nextLetter {
                    break
                }
                // letters the 🐢 walks past are no longer being tracked in the dynamic substring
                lettersBeingTracked.remove(s[🐢 - 1])
            }
        } else {
            // a new substring is encountered, so check it against the longest
            let currentSubstring: Substring = getSubstringFromIndices(s: s, start: 🐢, end: 🐇)
            if currentSubstring.count > longestSubstring.count {
                longestSubstring = currentSubstring
            }

            lettersBeingTracked.insert(nextLetter!)
        }
    }

    return longestSubstring.count
}

func getSubstringFromIndices(s: String, start: Int, end: Int) -> Substring {
    let startIndex = s.index(s.startIndex, offsetBy: start)
    let endIndex = s.index(s.endIndex, offsetBy: end - s.count - 1)
    return s[startIndex..<endIndex]
}

extension String {
    subscript (i: Int) -> Character {
        return self[index(startIndex, offsetBy: i)]
    }
}

// this will take at most 2 iterations on the characters of string s
// when a duplicate is found, the newest valid substring starts after the first instance of the duped letter, not the latest letter
// edge inputs: "au", "aab", "", extremely long inputs
