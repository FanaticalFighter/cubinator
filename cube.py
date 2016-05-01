from point import *
from rotation import *

class Sticker:
    def __init__(self, point, color):
        '''
        Initializes a sticker at point with the color represented by the string color
        '''

        self.point = point
        self.color = color

class Cube:
    def __init__(self):
        '''Initializes a cube in the default orientation'''

        self.stickers = []

        # Populate front face. All stickers on the front face have Z = 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.stickers.append(Sticker(Point(i, j, 2), 'green'))

        # Populate back face. All stickers on the back face have Z = - 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.stickers.append(Sticker(Point(i, j, - 2), 'blue'))

        # Populate top face. All stickers on the top face have Y = 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.stickers.append(Sticker(Point(i, 2, j), 'white'))

        # Populate down face. All stickers on the down face have Y = - 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.stickers.append(Sticker(Point(i, - 2, j), 'yellow'))

        # Populate left face. All stickers on the left face have X = - 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.stickers.append(Sticker(Point(- 2, i, j), 'orange'))

        # Populate right face. All stickers on the right face have X = - 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.stickers.append(Sticker(Point(2, i, j), 'red'))

    def __str__(self):
        print_str = ''

        print_str += 'Left face:\n'
        for i in range(-1, 2):
            for j in range(-1, 2):
                print_str += self._find_sticker_at(Point(- 2, i, j)).color[:1]
            print_str += '\n'
        print_str += '\n'

        print_str += 'Right face:\n'
        for i in range(-1, 2):
            for j in range(-1, 2):
                print_str += self._find_sticker_at(Point(2, i, j)).color[:1]
            print_str += '\n'
        print_str += '\n'

        print_str += 'Up face:\n'
        for i in range(-1, 2):
            for j in range(-1, 2):
                print_str += self._find_sticker_at(Point(i, 2, j)).color[:1]
            print_str += '\n'
        print_str += '\n'

        print_str += 'Down face:\n'
        for i in range(-1, 2):
            for j in range(-1, 2):
                print_str += self._find_sticker_at(Point(i, -2, j)).color[:1]
            print_str += '\n'
        print_str += '\n'

        print_str += 'Front face:\n'
        for i in range(-1, 2):
            for j in range(-1, 2):
                print_str += self._find_sticker_at(Point(i, j, 2)).color[:1]
            print_str += '\n'
        print_str += '\n'

        print_str += 'Back face:\n'
        for i in range(-1, 2):
            for j in range(-1, 2):
                print_str += self._find_sticker_at(Point(i, j, -2)).color[:1]
            print_str += '\n'
        print_str += '\n'

        return print_str


    def _find_sticker_at(self, point):
        '''Finds and returns a sticker at point'''
        for sticker in self.stickers:
            if sticker.point.position == point.position:
                return sticker

        return None

    def _get_layer(self, layer):
        '''Returns the indexes of all the stickers that would be turned when
        turning the layer defined by the string layer.

        e.g. get_layer ('R') returns all the stickers on the right face and
        also all the stickers immediately bordering the R face. '''

        indexes = []
        if layer == 'R':
            for elem, index in zip (self.stickers, range(len(self.stickers))):
                if elem.point.position[0] >= 1:
                    indexes.append(index)

        if layer == 'L':
            for elem, index in zip (self.stickers, range(len(self.stickers))):
                if elem.point.position[0] <= - 1:
                    indexes.append(index)

        if layer == 'U':
            for elem, index in zip (self.stickers, range(len(self.stickers))):
                if elem.point.position[1] >= 1:
                    indexes.append(index)

        if layer == 'D':
            for elem, index in zip (self.stickers, range(len(self.stickers))):
                if elem.point.position[1] <= - 1:
                    indexes.append(index)

        if layer == 'F':
            for elem, index in zip (self.stickers, range(len(self.stickers))):
                if elem.point.position[2] >= 1:
                    indexes.append(index)

        if layer == 'B':
            for elem, index in zip (self.stickers, range(len(self.stickers))):
                if elem.point.position[2] <= -1:
                    indexes.append(index)

        return indexes

    def perform_move(self, move):
        '''
        Parses 'move' as a move string (e.g R' or D etc. and performs it on the
        cube)
        '''

        layer = move[0]

        counter_clockwise = False
        if len(move) > 1 and move[1] == "'":
            counter_clockwise = True

        indexes = self._get_layer(layer)

        if layer == 'R' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_x_counter_clockwise(self.stickers[i].point)

        if layer == 'R' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_x_clockwise(self.stickers[i].point)

        if layer == 'L' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_x_clockwise(self.stickers[i].point)

        if layer == 'L' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_x_counter_clockwise(self.stickers[i].point)

        if layer == 'U' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_y_counter_clockwise(self.stickers[i].point)

        if layer == 'U' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_y_clockwise(self.stickers[i].point)

        if layer == 'D' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_y_clockwise(self.stickers[i].point)

        if layer == 'D' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_y_counter_clockwise(self.stickers[i].point)

        if layer == 'F' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_z_counter_clockwise(self.stickers[i].point)

        if layer == 'F' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_z_clockwise(self.stickers[i].point)

        if layer == 'B' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_z_clockwise(self.stickers[i].point)

        if layer == 'B' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = rotate_about_z_counter_clockwise(self.stickers[i].point)
