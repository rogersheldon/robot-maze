
# Returns an (angle, leftRight, distance) tuple for navigating a robot
# from fromCoordinate to toCoordinate with an initial direction of angle.
def navigate(angle, fromCoordinate, toCoordinate):
    print(fromCoordinate)
    print(toCoordinate)
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