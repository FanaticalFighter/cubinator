class Point:
    '''
    Represents a point in 3D space
    '''
    def __init__(self):
        self.position = [0, 0, 0]

    def __init__(self, x, y, z):
        '''
        Constructs a point located at the co-ordinates (x, y, z)
        '''
        self.position = [x, y, z]

    def return_rotation(self, rotation_matrix):
        p = Point(0, 0, 0)

        for i in range(3):
            for j in range(3):
                p.position[i] += rotation_matrix[i][j] * self.position[j]

        return p
