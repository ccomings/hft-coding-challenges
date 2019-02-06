import sys
import math
import operator

# mschettler nov 2018
# compute risk for pawn, increasing =
# Save humans, destroy zombies!
def mean(a):
    # use weighted mean with distances to humans
    return float(sum(a)) / float(len(a))

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)


def does_circle_contain_point(cp, r, p0):
    return (p0[0]-cp[0])**2 + (p0[1] - cp[1])**2 < r**2

guarding_court = False
court_lock = None


ASH_RANGE = 2000
tick_count = 0
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
    if 0 and len(nearby_court_members) > 2:
        # there is a court nearby
        # adjust king circle to cover court
        king_hum_x = median([h[0] for h in nearby_court_members])
        king_hum_y = median([h[1] for h in nearby_court_members])
        guarding_court = True
        if not court_lock:
            court_lock = (king_hum_x, king_hum_y)


    king_cloest_zom_distance = k[-1][1]
    # compute king danger 1-10 (10 is alot of danger)
    king_danger = max(0, 10 - (king_cloest_zom_distance/1000.0))

    avg_hum_x = king_hum_x
    avg_hum_y = king_hum_y

    avg_zom_x = median(zom_x)
    avg_zom_y = median(zom_y)

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

    if guarding_court:
        # we are guarding court; need to stay near.
        hum_per = 1.0

    target_x = sum([
         avg_hum_x * hum_per,
         avg_zom_x * (1.0 - hum_per),
    ])
    target_y = sum([
         avg_hum_y * hum_per,
         avg_zom_y * (1.0 - hum_per),
    ])

    if guarding_court:
        mode = 'court'
    else:
        if king_danger > 8:
            # super safe mode
            mode = 'save king'
            # saving king, but hes part of a court
            if court_lock:
                mode = 'save king CL'
                target_x, target_y = court_lock

        elif king_danger < 5 or (tick_count <= 5 or tick_count >= 26): # roughly first half of game
            mode = 'hunt'
        else:
            mode = 'hybrid'

    guarding_court = False

    # when hunting, dont move backwards

    # if we are in hunter mode, and there is a zombie between us and our king, aim towards that zombie

    print >> sys.stderr, 'tick count: {}'.format(tick_count)
    print >> sys.stderr, 'king danger: {}'.format(king_danger)
    print >> sys.stderr, 'hum weight: {}'.format(hum_per)
    print >> sys.stderr, 'mode: {}'.format(mode)


    print "{x} {y} {status}".format(
        x=int(target_x),
        y=int(target_y),
        status=mode,
    )
    tick_count += 1
