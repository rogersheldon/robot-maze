import math

# Returns an (angle, leftRight, distance) tuple for navigating a robot
# from fromCoordinate to toCoordinate with an initial direction of angle.
def navigate(angle, fromCoordinate, toCoordinate):
    # print(fromCoordinate)
    # print(toCoordinate)
    #           to
    #           /|
    #          /b|
    #    hyp  /  |
    #        /   | opp
    #       /a   |
    #      /-----|
    #  from  adj

    print(f'---------------')
    print(f'{angle} {fromCoordinate} {toCoordinate}')
    x1 = fromCoordinate[0]
    x2 = toCoordinate[0]
    y1 = fromCoordinate[1]
    y2 = toCoordinate[1]
    adj = x2 - x1
    opp = y2 - y1
    hyp = math.sqrt(adj**2 + opp**2)
    angleRadians = math.atan(opp / adj)
    angle = math.degrees(angleRadians)
    # print(x1, x2, y1, y2, adj, opp, hyp)
    print(adj, opp, hyp, angle)
    leftRight = 'right' if angle < 0 else 'left'
    return(angle, leftRight, hyp)
    
def main():
    coordinates = [ (0, 0), (25, 0), (38, 13), (28, 38) ]
    angle = 0.0
    
    for i in range(len(coordinates) - 1): # Loop through pairs of coordinates
        fromCoordinate = coordinates[i]
        toCoordinate = coordinates[i + 1]
        (angle, leftRight, distance) = navigate(angle, fromCoordinate, toCoordinate)
        print('From', fromCoordinate, 'turn', angle, 'degrees', leftRight, 'and move forward', distance, 'units to', toCoordinate)


main()