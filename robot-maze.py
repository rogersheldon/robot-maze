import math

# Returns an (angle, leftRight, distance) tuple for navigating a robot
# from fromCoordinate to toCoordinate with an initial direction of angle.
def navigate(angle, fromCoordinate, toCoordinate):
    # print(fromCoordinate)
    # print(toCoordinate)
    #
    #         /|
    #        /b|
    #       /  |
    # hyp  /   | opp
    #     /a   |
    #     ------
    #      adj
    x1 = fromCoordinate[0]
    x2 = toCoordinate[0]
    y1 = fromCoordinate[1]
    y2 = toCoordinate[1]
    adj = x2 - x1
    opp = y2 - y1
    # adj^2 + opp^2 = hyp^2
    # print(adj**2)
    # print(opp**2)
    # print((adj**2 + opp**2))
    x = (adj**2) + (opp**2)
    # print(x)
    # print((adj**2 + opp**2))
    hyp = math.sqrt(adj**2 + opp**2)
    # print(x1, x2, y1, y2, adj, opp, hyp)
    print(adj, opp, hyp)

    return(10.0, 'left', 20.0)
    
def main():
    coordinates = [ (0, 0), (25, 0), (38, 13) ]
    angle = 0.0
    
    for i in range(len(coordinates) - 1): # Loop through pairs of coordinates
        fromCoordinate = coordinates[i]
        toCoordinate = coordinates[i + 1]
        (angle, leftRight, distance) = navigate(angle, fromCoordinate, toCoordinate)
        print('From', fromCoordinate, 'turn', angle, 'degrees', leftRight, 'and move forward', distance, 'units to', toCoordinate)


main()