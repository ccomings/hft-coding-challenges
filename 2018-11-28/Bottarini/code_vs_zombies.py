import sys
import math

# Save humans, destroy zombies!
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# game loop
while True:
    closest_human = None
    closest_human_distance = 9e9
    closest_nom_distance = 9e9
    human_coords = []
    zombie_coords = []
    DISTANCE_HUMAN_IS_NOM = 400
    
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        human_coords.append((human_x, human_y))
                   
    zombie_count = int(raw_input())
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombie_coords.append((zombie_x, zombie_y))
        
    print >> sys.stderr, "{} {}".format(human_coords, zombie_coords)
    
    # compute the closest human
    for human in human_coords:
        is_nom_nom = False
        distance_to_ash = distance((human[0], human[1]), (x,y))
        for zombie in zombie_coords:
            distance_to_zombie = distance((human[0], human[1]), (zombie[0], zombie[1]))
            print >> sys.stderr, "{}".format(distance_to_zombie)
            if distance_to_zombie <= DISTANCE_HUMAN_IS_NOM:
                # ast.literal_eval(human) = "BURRRPPP!!!"
                is_nom_nom = True
                break
        if is_nom_nom:
            continue
        
        if distance_to_ash < closest_human_distance:
            closest_human_distance = distance_to_ash
            closest_human = human
            
    if not closest_human:
        closest_human = (x,y)
            
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # Your destination coordinates
    print "{} {}".format(closest_human[0], closest_human[1])