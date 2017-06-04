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


# __str__ function gives the ability to print out the coordinates of the vector
# with Python's built in print function
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

# __eq__ functions allows us to test if 2 Vectors are equal
    def __eq__(self, v):
        return self.coordinates == v.coordinates


my_vector = Vector([1,2,3])
print (my_vector)
my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])

print(my_vector == my_vector3)