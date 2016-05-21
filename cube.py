from point import *
from rotation import *
import kociemba
import serial
import sequence_decomposer as sd
import cv.cv as cv
import urllib2


def main():
    c = build_cube_from_webcam()
    string = c.get_kociemba_string()
    solve_str = kociemba.solve(string)
    solve_str = sd.decompose_sequence(solve_str)

    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

    moves = solve_str.split(' ')
    for move in moves:
        ser.write(move)

        ser.readline()  # wait for move completed response
        raw_input()  # wait for user input


def get_image(imgname, url):

    f = urllib2.urlopen(url)
    print("Reading from " + url)
    data = f.read()
    with open(imgname, 'wb') as img:
        img.write(data)


def build_cube_from_webcam():
    c = Cube()

    imgname = "photoaf.jpg"

    # url = raw_input("Enter WebCam IP = ")
    url = "192.168.43.1:8080"
    url = "http://" + url + "/photoaf.jpg"

    # TODO add code to send moves to arduino here

    while(True):
        get_image(imgname, url)
        c.color_down_face(imgname)  # yellow face
        i = raw_input()
        if i != 'r':
            break

    c.perform_move('z')  # go to red face on down
    while(True):
        get_image(imgname, url)
        c.color_down_face(imgname)
        i = raw_input()
        if i != 'r':
            break

    c.perform_move('z')  # go to white face on down
    while(True):
        get_image(imgname, url)
        c.color_down_face(imgname)
        i = raw_input()
        if i != 'r':
            break

    c.perform_move('z')  # go to orange face on down
    while(True):
        get_image(imgname, url)
        c.color_down_face(imgname)
        i = raw_input()
        if i != 'r':
            break

    c.perform_move('x')  # go to blue face on down
    while(True):
        get_image(imgname, url)
        c.color_down_face(imgname)
        i = raw_input()
        if i != 'r':
            break

    c.perform_move_sequence('x x')  # go to green face on down
    while(True):
        get_image(imgname, url)
        c.color_down_face(imgname)
        i = raw_input()
        if i != 'r':
            break

    c.perform_move_sequence('x z')  # return to white on top, green on front

    return c

class Sticker:
    def __init__(self, point, color):
        '''
        Initializes a sticker at point with the color and point'''

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

    def _get_all_indices(self):
        '''
        Returns all the indices in the cube
        '''

        indices = []
        for elem, index in zip(self.stickers, range(len(self.stickers))):
            indices.append(index)

        return indices

    def _get_layer(self, layer):
        '''Returns the indexes of all the stickers that would be turned when
        turning the layer defined by the string layer.

        e.g. get_layer ('R') returns all the stickers on the right face and
        also all the stickers immediately bordering the R face. '''

        indexes = []
        if layer == 'R':
            for elem, index in zip(self.stickers, range(len(self.stickers))):
                if elem.point.position[0] >= 1:
                    indexes.append(index)

        if layer == 'L':
            for elem, index in zip(self.stickers, range(len(self.stickers))):
                if elem.point.position[0] <= - 1:
                    indexes.append(index)

        if layer == 'U':
            for elem, index in zip(self.stickers, range(len(self.stickers))):
                if elem.point.position[1] >= 1:
                    indexes.append(index)

        if layer == 'D':
            for elem, index in zip(self.stickers, range(len(self.stickers))):
                if elem.point.position[1] <= - 1:
                    indexes.append(index)

        if layer == 'F':
            for elem, index in zip(self.stickers, range(len(self.stickers))):
                if elem.point.position[2] >= 1:
                    indexes.append(index)

        if layer == 'B':
            for elem, index in zip(self.stickers, range(len(self.stickers))):
                if elem.point.position[2] <= -1:
                    indexes.append(index)

        return indexes

<<<<<<< HEAD
    def get_kociemba_string(self):
        '''
        Returns a string in the format that the kociemba library accepts
        See more here: https://github.com/muodov/kociemba
        '''

        colors = {
            'white': 'U',
            'green': 'F',
            'yellow': 'D',
            'orange': 'L',
            'red': 'R',
            'blue': 'B'
        }

        kociemba_str = ''
        self.perform_move("x'")  # go to up face

        for j in range(1, -2, -1):
            for i in range(-1, 2):
                s = self._find_sticker_at(Point(i, j, 2))
                kociemba_str += colors[s.color]

        self.perform_move_sequence("x y")  # go to right face

        for j in range(1, -2, -1):
            for i in range(-1, 2):
                s = self._find_sticker_at(Point(i, j, 2))
                kociemba_str += colors[s.color]

        self.perform_move("y'")  # go to front face

        for j in range(1, -2, -1):
            for i in range(-1, 2):
                s = self._find_sticker_at(Point(i, j, 2))
                kociemba_str += colors[s.color]

        self.perform_move("x")  # go to down face

        for j in range(1, -2, -1):
            for i in range(-1, 2):
                s = self._find_sticker_at(Point(i, j, 2))
                kociemba_str += colors[s.color]

        self.perform_move_sequence("x' y'")  # go to left face

        for j in range(1, -2, -1):
            for i in range(-1, 2):
                s = self._find_sticker_at(Point(i, j, 2))
                kociemba_str += colors[s.color]

        self.perform_move_sequence("y'")  # go to back face

        for j in range(1, -2, -1):
            for i in range(-1, 2):
                s = self._find_sticker_at(Point(i, j, 2))
                kociemba_str += colors[s.color]

        self.perform_move_sequence("y y")  # go to back to the front face

        return kociemba_str
=======
    def color_down_face(self, imgname):
        '''
        Colors the down face from the image from imgname using cv
        '''

        colors = cv.return_face_colors(imgname)

        for i in range(-1, 2):
            for j in range(-1, 2):
                x = i + 1
                z = j + 1

                # all down stickers have y = -2
                s = _find_sticker_at(Point(i, -2, j))
                s.color = colors[x, z]

    def perform_move(self, move):
        '''
        Parses 'move' as a move string (e.g R' or D etc. and performs it on the
        cube)
        '''

        layer = move[0]

        counter_clockwise = False
        if len(move) > 1 and move[1] == "'":
            counter_clockwise = True

        if layer in ['x', 'y', 'z']:
            indexes = self._get_all_indices()
        else:
            indexes = self._get_layer(layer)

        if layer == 'x' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_x_counter_clockwise(self.stickers[i].point)
        if layer == 'x' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_x_clockwise(self.stickers[i].point)
        if layer == 'y' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_y_counter_clockwise(self.stickers[i].point)
        if layer == 'y' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_y_clockwise(self.stickers[i].point)
        if layer == 'z' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_z_counter_clockwise(self.stickers[i].point)
        if layer == 'z' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_z_counter_clockwise(self.stickers[i].point)

        if layer == 'R' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_x_counter_clockwise(self.stickers[i].point)

        if layer == 'R' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_x_clockwise(self.stickers[i].point)

        if layer == 'L' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_x_clockwise(self.stickers[i].point)

        if layer == 'L' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_x_counter_clockwise(self.stickers[i].point)

        if layer == 'U' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_y_counter_clockwise(self.stickers[i].point)

        if layer == 'U' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_y_clockwise(self.stickers[i].point)

        if layer == 'D' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_y_clockwise(self.stickers[i].point)

        if layer == 'D' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_y_counter_clockwise(self.stickers[i].point)

        if layer == 'F' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_z_counter_clockwise(self.stickers[i].point)

        if layer == 'F' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_z_clockwise(self.stickers[i].point)

        if layer == 'B' and not counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_z_clockwise(self.stickers[i].point)

        if layer == 'B' and counter_clockwise:
            for i in indexes:
                self.stickers[i].point = \
                    rotate_about_z_counter_clockwise(self.stickers[i].point)

    def perform_move_sequence(self, sequence):
        '''
        Splits a move sequence like "R U R' U R U U R" into seperate moves and
        applies them on the cube in order.
        '''

        moves = sequence.split(' ')
        for move in moves:
            self.perform_move(move)

<<<<<<< HEAD
if __name__ == '__main__':
    main()
=======
print "Building cube from webcam"
c = build_cube_from_webcam()
print c
>>>>>>> feature/cv-integration
