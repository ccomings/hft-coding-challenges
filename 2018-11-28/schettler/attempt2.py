import sys
import math
import operator

# Save humans, destroy zombies!

def avg(a):
    return float(sum(a)) / float(len(a))
    
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def same_sector(h, zlx, zly):
    """ return true if all zombie in in the xy same sector as the human """
    return same_sector_x(h, zlx) and same_sector_y(h, zly)

def same_sector_x(h, zlx):
    
    tx = zlx[0]
    
    if h[0] < tx:
        return all((h[0] <= x for x in zlx))
    elif h[0] > tx:        
        return all((h[0] >= x for x in zlx))
    return True
    
def same_sector_y(h, zly):
    
    ty = zly[0]
    
    if h[1] < ty:
        return all((h[1] <= y for y in zly))
    elif h[1] > ty:        
        return all((h[1] >= y for y in zly))
    return all((h[1] == y for y in zly))
    
    
    
    

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

    king_cloest_zom_distance = k[-1][1]
    # compute king danger 1-10 (10 is alot of danger)
    king_danger = max(0, 10 - (king_cloest_zom_distance/1000.0))

    avg_hum_x = king_hum_x
    avg_hum_y = king_hum_y
    
    avg_zom_x = avg(zom_x)
    avg_zom_y = avg(zom_y)

    mode = ''

    if len(zom_x) > 10 or king_danger > 6:
        # super safe mode
        mode = 'emergency'
        # calculate midpoint favoring human
        target_x = sum([
            avg_hum_x * 0.94,
            avg_zom_x * 0.06,
        ])
        target_y = sum([
            avg_hum_y * 0.94,
            avg_zom_y * 0.06,
        ])      
        
    elif len(zom_x) <= 20 and king_danger < 4:# and same_sector((king_hum_x, king_hum_y), zom_x, zom_y):
        # hunter mode
        mode = 'hunter'
        # calculate midpoint favoring zs
        target_x = sum([
            avg_hum_x * 0.10,
            avg_zom_x * 0.90,
        ])
        target_y = sum([
            avg_hum_y * 0.10,
            avg_zom_y * 0.90,
        ])
            
    else:
        mode = 'hybrid'
        # hybrid mode
        # calculate midpoint favoring human
        target_x = sum([
            avg_hum_x * 0.75,
            avg_zom_x * 0.25,
        ])
        target_y = sum([
            avg_hum_y * 0.75,
            avg_zom_y * 0.25,
        ])

    # Write an action using print
    # To debug: 

    # Your destination coordinates
    print "{} {} {} k:{}".format(int(target_x), int(target_y), mode, int(king_danger))
    #print "0 0"