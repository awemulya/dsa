class Vector(object):
    "Vector class represents vector of coordinates of any dimensions"

    def __init__(self, dimension):
        self._coordinates = [0] * dimension

    def __len__(self):
        return len(self._coordinates)

    def __str__(self):
        return '<' + str(self._coordinates) + '>'

    def __getitem__(self, index):
        if not len(self._coordinates) > index:
            raise IndexError("vector size less than given index")
        return self._coordinates[index]

    def __setitem__(self, key, value):
        self._coordinates[key] = value

    def __add__(self, other):
        if not len(self) == len(other):
            raise ValueError(" vector Must be of same dimensions to add")
        vector = Vector(len(self._coordinates))
        for i in range(len(self._coordinates)):
            vector[i] = self[i] + other[i]
        return vector

    def __sub__(self, other):
        if not len(self) == len(other):
            raise ValueError(" vector Must be of same dimensions to add")
        vector = Vector(len(self._coordinates))
        for i in range(len(self._coordinates)):
            vector[i] = self[i] - other[i]
        return vector

    def __eq__(self, other):
        return self._coordinates == other._coordinates

    def __ne__(self, other):
        return not self == other