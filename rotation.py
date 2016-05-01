from point import *
import math

def rotate_about_x_clockwise(point):
    rotation_matrix = [[1, 0, 0],
                       [0, 0, -1],
                       [0, 1, 0]]

    return point.return_rotation(rotation_matrix)

def rotate_about_x_counter_clockwise(point):
    rotation_matrix = [[1, 0, 0],
                       [0, 0, 1],
                       [0, -1, 0]]

    return point.return_rotation(rotation_matrix)

def rotate_about_y_clockwise(point):
    rotation_matrix = [[0, 0, 1],
                       [0, 1, 0],
                       [-1, 0, 0]]

    return point.return_rotation(rotation_matrix)

def rotate_about_y_counter_clockwise(point):
    rotation_matrix = [[0, 0, -1],
                       [0, 1, 0],
                       [1, 0, 0]]

    return point.return_rotation(rotation_matrix)

def rotate_about_z_clockwise(point):
    rotation_matrix = [[0, -1, 0],
                       [1, 0, 0],
                       [0, 0, 1]]

    return point.return_rotation(rotation_matrix)

def rotate_about_z_counter_clockwise(point):
    rotation_matrix = [[0, 1, 0],
                       [-1, 0, 0],
                       [0, 0, 1]]

    return point.return_rotation(rotation_matrix)
