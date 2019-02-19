################################################################################
# mschettler nov 2018
# compute risk for pawn, increasing =
# Save victims, destroy zombies!
################################################################################
import sys
import math
import operator


################################################################################
# Globals
################################################################################

guarding_court = False
court_lock = None

ASH_RANGE = 2000
ASH_PIXELS_PER_TICK = 1000
ZOMBIE_PIXELS_PER_TICK = 400

# king danger is a 0-10 ranking, 10 means he is in the most danger
# we map danger to a % of how close to the king he should be based
# on the danger. ie a danger of 10 means he should be 96% near the king
KING_DANGER_MAP = {
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

################################################################################
# Helpers
################################################################################
def mean(a):
    # use weighted mean with distances to victims FIXME?
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


################################################################################
# Classes
################################################################################
class Unit(object):

    pk = None
    x = None
    y = None

    def from_coord(self, pk, x, y):
        self.pk = pk
        self.x = x
        self.y = y
        return self

    @property
    def center(self):
        return (self.x, self.y)

    def __str__(self):
        return "[{} (id:{}, x:{}, y:{})]".format(type(self).__name__, self.pk, self.x, self.y)


class Ash(Unit):
    pass


class Zombie(Unit):

    next_x = None
    next_y = None

    def from_coord(self, pk, x, y, next_x, next_y):
        self.pk = pk
        self.x = x
        self.y = y
        self.next_x = next_x
        self.next_y = next_y
        return self

    @property
    def next_center(self):
        return (self.next_x, self.next_y)


class Victim(Unit):

    def get_nearest_zombie(self, zombies):
        ret = None  # return a zombie
        c_zombie = None  # distance that is the closest so far
        for z in zombies:
            d = distance(self.center, z.center)
            if c_zombie is None:
                c_zombie = d
                ret = z
            else:
                if d < c_zombie:
                    c_zombie = d
                    ret = z
        return (ret, c_zombie)


class ZombieGame(object):

    tick = 0

    def read_game_info(self):
        """ using the code they gave us, read the game info from stdin
            then, allocate our game objects and return them
        """

        x, y = [int(i) for i in raw_input().split()]
        ash = Ash().from_coord(1, x, y)

        victim_count = int(raw_input())
        victims = []
        for i in xrange(victim_count):
            victim_id, victim_x, victim_y = [int(j) for j in raw_input().split()]
            victims.append(Victim().from_coord(victim_id, victim_x, victim_y))

        zombie_count = int(raw_input())
        zombies = []
        for i in xrange(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
            zombies.append(Zombie().from_coord(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))

        self.tick += 1

        return ash, zombies, victims

    def find_already_dead_victims(self, victims, zombies, ash):
        # return any victims in victims that cant be saved.
        # ie ash is too far away

        already_dead = []

        for v in victims:

            # get ash distance from victim
            ash_distance = distance(ash.center, v.center)

            # subtract ash gun range
            ash_distance -= ASH_RANGE

            # if this is negative, ash is in range, and we can continue for efficiency
            if ash_distance < 0:
                continue

            # find nearest zombie
            nearest_zombie, nearest_distance = v.get_nearest_zombie(zombies)

            # ash travels twice as fast; so halve the distance he needs to travel
            ash_ticks_needed = ash_distance / ASH_PIXELS_PER_TICK
            z_ticks_needed = nearest_distance / ZOMBIE_PIXELS_PER_TICK

            if z_ticks_needed < ash_ticks_needed:
                already_dead.append(v)

        return already_dead

    def are_all_zombies_in_range_of_eachother(self, zombies, ash):
        search_z = zombies[0]  # FIXME should be closest zombie to ash
        for z in zombies[1:]:
            d = distance(search_z.center, z.center)
            if d > ASH_RANGE:
                return False
        return True


# game loop
zg = ZombieGame()
king = None
while True:

    ash, zombies, victims = zg.read_game_info()

    already_dead = zg.find_already_dead_victims(victims, zombies, ash)

    print >> sys.stderr, "we have {} victims already dead {}".format(len(already_dead), [v.pk for v in already_dead])

    # map victim to the nearest zombie
    victim_zdistance_map = {v: v.get_nearest_zombie(zombies) for v in victims if v not in already_dead}
    if not victim_zdistance_map:
        # allow already dead
        victim_zdistance_map = {v: v.get_nearest_zombie(zombies) for v in victims}

    # sort by value
    victim_zdistance_sorted = sorted(victim_zdistance_map.items(), key=operator.itemgetter(1))

    victim_centers = [v.center for v in victims if v not in already_dead]
    if king and not king.center in victim_centers:
        # king died
        king = None

    # pick king. king is safest victim (its closest zombie is further than the other victims)
    if not king:
        king = victim_zdistance_sorted[-1][0]
        # get the distance to the kings biggest threat
        king_closest_zom_distance = victim_zdistance_sorted[-1][1][1]
    else:
        # king is already set, just compute distance
        _, king_closest_zom_distance = king.get_nearest_zombie(zombies)
    #[(<__main__.Victim object at 0x7f7bbf861450>, (<__main__.Zombie object at 0x7f7bbf861410>, 4499.0))]


    # compute king danger 1-10 (10 is alot of danger)
    king_danger = max(0, 10 - (king_closest_zom_distance/1000.0))

    # adjust king danger based on player distance to king
    distance_from_king = distance(ash.center, king.center)

    add_me = distance_from_king / 3000
    print >> sys.stderr, 'add_me: {}'.format(add_me)
    king_danger += add_me
    king_danger = min(10, king_danger)

    print >> sys.stderr, "dk: {}".format(distance_from_king)

    avg_zom_x = median([z.x for z in zombies])
    avg_zom_y = median([z.y for z in zombies])

    hum_per = float(KING_DANGER_MAP[int(round(king_danger,0))]) / 100.0

    if king_danger >= 8:
        # super safe
        mode = 'save king'
        target_x, target_y = king.center

    elif len(zombies) <= 4:

        # kill closest zombie
        minn = 9999999
        thez = None
        for z in zombies:
            d = distance(ash.center, z.next_center)
            if d < minn:
                minn = d
                thez = z

        mode = 'closest z'
        target_x, target_y = thez.next_center

    elif zg.are_all_zombies_in_range_of_eachother(zombies, ash):
        # 5 or more zombies in a single group

        # FIXME compute optimal path

        # kill furthest zombie
        maxx = 1
        thez = None
        for z in zombies:
            d = distance(ash.center, z.next_center)
            if d > maxx:
                maxx = d
                thez = z

        mode = 'group splat'
        target_x, target_y = thez.next_center

    elif king_danger < 2.5:
        # its very safe, just go hunting
        mode = 'safe hunt'
        hum_per = 0.15
        target_x = sum([
             king.x * hum_per,
             avg_zom_x * (1.0 - hum_per),
        ])
        target_y = sum([
             king.y * hum_per,
             avg_zom_y * (1.0 - hum_per),
        ])

    elif king_danger < 6.0 and len([v for v in victims if v not in already_dead]) >= 2:
    # if king is safe, and 2 alive victims we try to look for the most "at risk" victim and save them

        mode = 'rescue'
        # most at
        risky_victim = victim_zdistance_sorted[0][0]

        target_x, target_y = risky_victim.center

        # # hmm
        # target_x -= (0.7 * ASH_RANGE)
        # target_y -= (0.7 * ASH_RANGE)

        # target_x = max(0, target_x)
        # target_y = max(0, target_y)

    else:

        mode = 'hybrid'

        target_x = sum([
             king.x * hum_per,
             avg_zom_x * (1.0 - hum_per),
        ])
        target_y = sum([
             king.y * hum_per,
             avg_zom_y * (1.0 - hum_per),
        ])
    # if all zombies are within ash range of each other, attack


    # if guarding_court:
    #     mode = 'court'
    # else:

    #     # saving king, but hes part of a court
    #     # if court_lock:
    #     #     mode = 'save king CL'
    #     #     target_x, target_y = court_lock

    # elif king_danger < 5 or (zg.tick <= 5 or zg.tick >= 26): # roughly first half of game
    #     mode = 'hunt'
    # else:
    #     mode = 'hybrid'

    # num_victims_worth_saving = 1
    # status = '{}'.format(num_victims_worth_saving)

    # guarding_court = False

    # when hunting, dont move backwards FIXME

    # if we are in hunte, and there is a zombie between us and our king, aim towards that zombie





    print >> sys.stderr, 'tick count: {}'.format(zg.tick)
    print >> sys.stderr, 'king: {}'.format(king)
    print >> sys.stderr, 'king danger: {}'.format(king_danger)
    print >> sys.stderr, 'hum weight: {}'.format(hum_per)
    print >> sys.stderr, 'mode: {}'.format(mode)


    print "{x} {y} {mode}".format(
        x=int(target_x),
        y=int(target_y),
        mode=mode,
    )


# 29k
