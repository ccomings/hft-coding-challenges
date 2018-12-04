################################################################################
# Matt Schettler
# Nov 2018
# https://www.codingame.com/multiplayer/optimization/code-vs-zombies
#
# Save victims, destroy zombies!
# 52920
#
################################################################################
import sys
import math
import operator


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
# Globals
################################################################################
ASH_RANGE = 2000
ASH_PIXELS_PER_TICK = 1000
ZOMBIE_PIXELS_PER_TICK = 400
BOARD_WIDTH = 16000
BOARD_HEIGHT = 9000
ORIGIN = (0, 0)
BOARD_MAX_DISTANCE = distance(ORIGIN, (BOARD_WIDTH, BOARD_HEIGHT))


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

    def __eq__(self, other):
        try:
            return self.pk == other.pk
        except AttributeError:
            return False


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

    def get_nearest_victim(self, victims):
        ret = None  # return a victim
        c_victim = BOARD_MAX_DISTANCE  # distance that is the closest so far
        for v in victims:
            d = distance(self.center, v.center)
            if d < c_victim:
                c_victim = d
                ret = v
        return (ret, c_victim)


class Victim(Unit):

    def get_victim_importance(self, king):
        return distance(king.center, self.center) // ASH_RANGE

    def get_nearest_zombie(self, zombies):
        ret = None  # return a zombie
        c_zombie = BOARD_MAX_DISTANCE  # distance that is the closest so far
        for z in zombies:
            d = distance(self.center, z.center)
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

            # ash travels faster
            ash_ticks_needed = ash_distance / ASH_PIXELS_PER_TICK
            z_ticks_needed = nearest_distance / ZOMBIE_PIXELS_PER_TICK

            if z_ticks_needed < ash_ticks_needed:
                already_dead.append(v.pk)

        return already_dead

    def are_all_zombies_in_range_of_eachother(self, zombies, ash):
        search_z = ash.get_nearest_zombie(zombies)
        for z in zombies:
            if z == search_z:
                # skip
                continue
            d = distance(search_z.center, z.center)
            if d > ASH_RANGE:
                return False
        return True


    def elect_king(self, zombies, victims):
        # king is safest victim (its closest zombie is further than the other victims)
        # map victim to the nearest zombie

        try:
            victim_zdistance_map = {v: v.get_nearest_zombie(zombies) for v in victims}
            victim_zdistance_sorted = sorted(victim_zdistance_map.items(), key=operator.itemgetter(1))
            king = victim_zdistance_sorted[-1][0]
            # get the distance to the kings biggest threat, saving a computation 
            king_closest_zom_distance = victim_zdistance_sorted[-1][1][1]
            return king, king_closest_zom_distance
        except IndexError:
            pass
        return None, None

    def compute_king_danger(self, king, ash, closest_zom_distance):

        # # compute king danger 1-10 (10 is alot of danger), return the danger index
        # # and the distance from king ash is
        # ret = max(0, 10 - (king_closest_zom_distance/1000.0))

        # # adjust king danger based on player distance to king
        # distance_from_king = distance(ash.center, king.center)
        # add_me = distance_from_king / 3000
        # zg.log('add_me: {}'.format(add_me))
        # ret += add_me
        # return min(10, ret), distance_from_king

        # king danger is how many ticks till the closest zombie gets em minus how many ticks away ash is


        zombie_ticks_away = (closest_zom_distance // ZOMBIE_PIXELS_PER_TICK) + 1
        ash_distance_from_king = distance(ash.center, king.center)
        ash_ticks_away = max((ash_distance_from_king - ASH_RANGE) // ASH_PIXELS_PER_TICK, -1) + 1

        if ash_ticks_away == zombie_ticks_away:
            # get there
            return 10, ash_distance_from_king

        if ash_ticks_away + 1 == zombie_ticks_away:
            # get there asap
            return 9, ash_distance_from_king

        return 0, ash_distance_from_king

    def compute_z_danger_index(self, zombie, zombies, victims, king):
        # return an integer expressing how much danger thsi zombie is causing

        humans_afraid_of_this_z = []#[v for v in victims if v.get_nearest_zombie(zombies) == zombie]

        v, v_distance = zombie.get_nearest_victim(victims)

        danger_list = [
            sum([h.get_victim_importance(king) for h in humans_afraid_of_this_z]),
            -distance(king.center, zombie.center) // ASH_PIXELS_PER_TICK,
            10000,
            len(humans_afraid_of_this_z)**2,
        ]
        danger = sum(danger_list)

        self.log('z={} is causing {} ={} danger'.format(zombie, danger_list, danger))
        return danger

    def log(self, m):
        print >> sys.stderr, m

    def save_king_coord(self, king):
        return king.center


# game loop
zg = ZombieGame()

king = None      # have we elected a king
split_count = 0  # how many frames in a row have we split

while True:

    ash, zombies, victims = zg.read_game_info()

    already_dead = zg.find_already_dead_victims(victims, zombies, ash)
    zg.log("we have {} victims already dead {}".format(len(already_dead), already_dead))
    
    # remove already dead from victims list entirely
    victims = [v for v in victims if v.pk not in already_dead]

    if king and not king.center in {v.center for v in victims}:
        # we had a king, but... now we dont. king died :'(
        king = None

    if not king:
        # elect king 
        king, king_closest_zom_distance = zg.elect_king(zombies, victims)

    else:
        # king is already set, simply compute distance to nearest zombie
        _, king_closest_zom_distance = king.get_nearest_zombie(zombies)

    if king:
        king_danger, ash_distance_king = zg.compute_king_danger(king, ash, king_closest_zom_distance)

        zg.log('king danger: {}'.format(king_danger))
        zg.log("ash dk: {}".format(ash_distance_king))
    else:
        zg.log('there is no king...')

    if len(zombies) == 1:

        # one zombie, just go kill it
        mode = 'cleanup'
        target_x, target_y = zombies[0].next_center

    elif len(zombies) == 2 and split_count >= 2:
        
        # two zombies we've split, cleanup
        mode = 'cleanup'
        target_x, target_y = zombies[0].next_center

    elif len(zombies) == 2 and distance(zombies[0].center, zombies[1].center) < (ASH_RANGE*4.0):

        # split difference
        mode = 'split'

        # find midpoint of ash and zombies next centers
        z1x, z1y = zombies[0].next_center
        z2x, z2y = zombies[1].next_center

        zx = mean([z1x, z2x])
        zy = mean([z1y, z2y])

        ax, ay = ash.center

        # form isocoleces triangle by draing right angle from midpoint
        h = ASH_RANGE

        theta = math.atan2(z2y - z1y, z2x - z1x)

        potential_targets = []
        for atheta in [theta+(math.pi / 2.0), theta+(3.0 * math.pi / 2.0)]:
            target_x = min(max(zx + (h * math.cos(atheta)), 0), 16000)
            target_y = min(max(zy + (h * math.sin(atheta)), 0), 9000)
            potential_targets.append((target_x, target_y))

        # compute distance for these points. choose the closer distance
        min_distance = BOARD_MAX_DISTANCE + 1
        for pt in potential_targets:
            d = distance(pt, ash.center)
            if d < min_distance:
                d = min_distance
                target_x, target_y = pt

    elif king_danger >= 9:

        # save our lord commander (by standing on him)
        mode = 'save king'
        target_x, target_y = zg.save_king_coord(king)

    else:

        # figure out which z is the most dangerous, and go hunt it
        mode = 'best z'

        danger_map = {z: zg.compute_z_danger_index(zombie=z, zombies=zombies, victims=victims, king=king) for z in zombies}
        danger_sorted = sorted(danger_map.items(), key=operator.itemgetter(1))

        zg.log(danger_sorted)

        # choose zombie with higest danger
        thez = danger_sorted[-1][0]
        zg.log(thez)
        target_x, target_y = thez.next_center
        
        # check if ash can kill only 1 zombie nxt turn , avoid FIXME

    if mode == 'split':
        split_count += 1
    else:
        split_count = 0
    
    zg.log('tick count: {}'.format(zg.tick))
    zg.log('king: {}'.format(king))
    zg.log('mode: {}'.format(mode))

    print "{x} {y} {mode}".format(
        x=int(target_x),
        y=int(target_y),
        mode=mode,
    )
