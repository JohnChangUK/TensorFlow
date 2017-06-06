from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))


    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)

        except ZeroDivisionError:
            raise Exception("Cannot normalize the Zero Vector")


    def plus(self, v):
        new_coordinates = [x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    # __str__ function gives the ability to print out the coordinates of the vector
# with Python's built in print function
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

# __eq__ functions allows us to test if 2 Vectors are equal
    def __eq__(self, v):
        return self.coordinates == v.coordinates

        