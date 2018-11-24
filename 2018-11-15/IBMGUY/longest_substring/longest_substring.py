class Solution(object):
    def lengthOfLongestSubstring(self, s):

        turtle_idx = 0
        hare_idx = 1

        # don't need to check inputs less than 2
        if len(s) < 2:
            return len(s)

        letters_being_tracked = set([s[0], s[1]])

        # default longest substring starts as length 2 unless the first two chars are the same
        if s[turtle_idx] == s[hare_idx]:
            longest_substring = s[hare_idx]
            turtle_idx += 1
        else:
            longest_substring = s[turtle_idx:hare_idx+1]

        while hare_idx < len(s):
            hare_idx += 1
            # check if the next letter will be a duplicate
            if hare_idx == len(s):
                next_letter = s[-1]
            else:
                next_letter = s[hare_idx]


            if next_letter in letters_being_tracked:
                # move the turtle up to the last time this repeating letter occurred
                while turtle_idx < hare_idx:
                    turtle_idx += 1
                    if s[turtle_idx - 1] == next_letter:
                        break

                    # remove previously seen letters after the turtle 'passes' them
                    letters_being_tracked.remove(s[turtle_idx - 1])
            else:
                # check substring against longest
                current_substring = s[turtle_idx:hare_idx + 1]

                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring

                letters_being_tracked.add(s[hare_idx])


        return len(longest_substring)


            
