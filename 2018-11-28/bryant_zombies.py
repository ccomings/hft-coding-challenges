import sys
import math


MAX_WIDTH = 16000
MAX_HEIGHT = 9000

ASH_ID = -1

ASH_MOVE = 1000
FIRE_RADIUS = 2000
ZOMBIE_MOVE = 400
ZOMBIE_RADIUS = 400

X = 0
Y = 1


def get_distance(x1, y1, x2, y2):
    """
    distance formula
    """
    x = x2 - x1
    y = y2 - y1
    return math.sqrt(x*x + y*y)


def triangulate(points):
    """
    return center of a list of points
    """
    x_total = 0
    y_total = 0
    for point in points:
        x_total += point[X]
        y_total += point[Y]

    total_points = len(points)
    return (x_total / total_points, y_total / total_points)


while True:
    x, y = [int(i) for i in raw_input().split()]

    humans = {}
    human_count = int(raw_input())
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        humans[human_id] = (human_x, human_y)
    humans[ASH_ID] = (x, y)

    zombies = {}
    zombie_count = int(raw_input())
    zombie_targets = {}
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombies[zombie_id] = (zombie_x, zombie_y)

        # target is None or (human_id, position, distance)
        target = None
        for human_id, position in humans.iteritems():
            distance = get_distance(zombie_x, zombie_y, position[X], position[Y])
            if target is None or distance < target[2]:
                target = (human_id, position, distance)

        if zombie_targets.get(target[0]) is None:
            zombie_targets[target[0]] = [(zombie_x, zombie_y, target[2])]
        else:
            zombie_targets[target[0]].append((zombie_x, zombie_y, target[2]))

        zombie_targets = {k: sorted(v, key=lambda x: x[2]) for k, v in zombie_targets.iteritems()}

    high = None
    priority_target = None
    pt_distance = None
    pt_distance_to_human = None
    pt_time_left = None
    for human_id, zombie_list in zombie_targets.iteritems():
        count = len(zombie_list)
        distance_to_human = zombie_list[0][2]
        center = triangulate(zombie_list)
        distance = get_distance(x, y, center[X], center[Y])

        time_left = distance_to_human / (ZOMBIE_MOVE + ZOMBIE_RADIUS)
        time_to = get_distance(x, y, center[X], center[Y]) / (ASH_MOVE + FIRE_RADIUS)
        if human_id != ASH_ID and time_left < time_to - 1:
            # Human can't be saved, don't prioritize
            continue

        if priority_target is None:
            priority_target = center
            pt_time_left = time_left
            pt_distance = distance
            pt_distance_to_human = distance_to_human
        elif human_id != ASH_ID and distance_to_human < pt_distance_to_human:
            priority_target = center
            pt_time_left = time_left
            priority_target_id = human_id
            pt_distance = distance
            pt_distance_to_human = distance_to_human
        elif high == count and count > high and distance < pt_distance:
            priority_target = center
            pt_time_left = time_left
            priority_target_id = human_id
            pt_distance = distance
            pt_distance_to_human = distance_to_human

    if priority_target is None:
        print "{} {}".format(x, y)
    else:
        print "{} {}".format(priority_target[0], priority_target[1])
