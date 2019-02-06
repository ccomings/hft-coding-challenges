import sys
import math
import operator

# mschettler nov 2018

# Save humans, destroy zombies!
def mean(a):
    return float(sum(a)) / float(len(a))


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def does_circle_contain_point(cp, r, p0):
    return (p0[0]-cp[0])**2 + (p0[1] - cp[1])**2 < r**2


ASH_RANGE = 2000
# game loop
while True:
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())

    hum_x = []
    hum_y = []

    king_hum_x = None
    king_hum_y = None
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]

        hum_x.append(human_x)
        hum_y.append(human_y)



    zombie_count = int(raw_input())


    zom_x = []
    zom_y = []


    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        #print >> sys.stderr, "Debug messages... {} {}".format(zombie_x, zombie_y)
        zom_x.append(zombie_x)
        zom_y.append(zombie_y)


    d_results = {}
    # pick king. king is safest human.
    for h in zip(hum_x, hum_y):
        c_zombie = 9999999
        for z in zip(zom_x, zom_y):
            c_zombie = min(c_zombie, distance(h, z))
        d_results[h] = c_zombie

    # sort by cloest zombie
    k = sorted(d_results.items(), key=operator.itemgetter(1))

    king_hum_x = k[-1][0][0]
    king_hum_y = k[-1][0][1]

    # if there are other humansn within gun range of this king, adjust king position to cover other humans as well

    nearby_court_members = [h for h in zip(hum_x, hum_y) if does_circle_contain_point((king_hum_x, king_hum_y), ASH_RANGE, h)]
    if len(nearby_court_members) > 1:
        # there is a court nearby
        # adjust king circle to cover court
        king_hum_x = mean(h[0] for h in nearby_court_members)
        king_hum_y = mean(h[1] for h in nearby_court_members)


    king_cloest_zom_distance = k[-1][1]
    # compute king danger 1-10 (10 is alot of danger)
    king_danger = max(0, 10 - (king_cloest_zom_distance/1000.0))

    avg_hum_x = king_hum_x
    avg_hum_y = king_hum_y

    avg_zom_x = mean(zom_x)
    avg_zom_y = mean(zom_y)

    king_danger_map = {
        0: 8,
        1: 10,
        2: 12,
        3: 20,
        4: 30,
        5: 45,
        6: 65,
        7: 78,
        8: 85,
        9: 92,
        10: 96,
    }

    # quadratic regression
    # 0 5 10 -> 10 75 92
    hum_per = float(king_danger_map[int(round(king_danger,0))]) / 100.0


    target_x = sum([
         avg_hum_x * hum_per,
         avg_zom_x * (1.0 - hum_per),
    ])
    target_y = sum([
         avg_hum_y * hum_per,
         avg_zom_y * (1.0 - hum_per),
    ])

    if king_danger > 6:
        # super safe mode
        mode = 'emergency'
    elif king_danger < 4:
        mode = 'hunter'
    else:
        mode = 'hybrid'

    # if we are in hunter mode, and there is a zombie between us and our king, aim towards that zombie


    print "{x} {y} {status}".format(
        x=int(target_x),
        y=int(target_y),
        status='{} k:{} h:{}'.format(mode, int(round(king_danger,0)), hum_per),
    )
