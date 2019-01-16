# --- Day 3: No Matter How You Slice It ---
# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.
#
# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.
#
# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:
#
# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
#
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:
#
# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

from collections import defaultdict


lines = [line.rstrip("\n") for line in open("day3input.txt")]

def convert_line(string):
    string_array = string.split(" ")
    claim_number = [string_array[0].strip("#")]
    starting_coord = string_array[2].strip(":").split(",")
    fabric_size = string_array[3].split("x")
    return claim_number + starting_coord + fabric_size

def check_fabric(array):
    fabric_map = [[0 for i in range(1000)] for j in range(1000)]
    for item in array:
        coords = convert_line(item)
        rows = int(coords[4])
        cols = int(coords[3])
        start_row = int(coords[2])
        start_col = int(coords[1])
        for m in range(rows):
            for n in range(cols):
                fabric_map[start_row + m][start_col + n] += 1

    counter = 0

    for a in range(len(fabric_map)):
        for b in range(len(fabric_map[a])):
            if int(fabric_map[a][b]) > 1:
                counter += 1

    print counter

check_fabric(lines)

def find_the_one(array):
    fabric_map = [[0 for i in range(1000)] for j in range(1000)]
    for item in array:
        coords = convert_line(item)
        rows = int(coords[4])
        cols = int(coords[3])
        start_row = int(coords[2])
        start_col = int(coords[1])
        claim = int(coords[0])
        for m in range(rows):
            for n in range(cols):
                if fabric_map[start_row + m][start_col + n] != 0:
                    fabric_map[start_row + m][start_col + n] = False
                else:
                    fabric_map[start_row + m][start_col + n] = claim

    counter = defaultdict(int)

    for a in range(len(fabric_map)):
        for b in range(len(fabric_map[a])):
            counter[fabric_map[a][b]] += 1

    # print fabric_map
    for item in array:
        coords = convert_line(item)
        claim = int(coords[0])
        rows = int(coords[4])
        cols = int(coords[3])

        if counter[claim] == rows * cols:
            print coords, claim

find_the_one(lines)
