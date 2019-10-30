
print('hello world')

print('done')

# class Coordinate:

# Returns an (angle, distance) tuple for navigating a robot
# from fromCoordinate to toCoordinate with an initial direction of angle.
def navigate(angle, fromCoordinate, toCoordinate):
    print(fromCoordinate)
    print(toCoordinate)
    return(10.0, 20.0)

def main():
    coordinates = [ (0, 0), (25, 0), (38, 13) ]
    angle = 0.0
    for i in range(len(coordinates) - 1):
        fromCoordinate = coordinates[i]
        toCoordinate = coordinates[i + 1]
        (angle, distance) = navigate(angle, fromCoordinate, toCoordinate)
        print('Turn ', angle, 'degrees and move forward', distance, 'units')


main()