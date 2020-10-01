# Lucas Weakland
# Homework 7
# Week 6
# I keep using "//" for comments and breaking my code instead of "#"
# imports
import inline as inline
import numpy as np
import math
import random
import matplotlib.pyplot as plt

# data
print("Printing The Example File: ")
with open('data', 'r') as f:
    f_contents = f.read(10000)
    print(f_contents, end='')

    f_contents = f.read(10000)
    print(f_contents, end='')

    f_contents = f.read(10000)
    print(f_contents, end='')

# Euclidean distance
point_a = np.array((5, 2, 4, 1, 60, 420))
point_b = np.array((2, 8, 3, 7, 3, 10))

distance = np.linalg.norm(point_a - point_b)
print("Printing Euclidean Distance: ")
print(distance)



# sum of manhattan distance below
def distancesum(a, b, n):
    sum = 0

    # for each point, finding distance to rest of the point
    for i in range(n):
        for j in range(i + 1, n):
            sum += (abs(a[i] - a[j]) +
                    abs(b[i] - b[j]))

    return sum


# Driven Code
a = [5, 2, 4, 1, 60, 420]
b = [2, 8, 3, 7, 3, 10]
n = len(a)
print("Printing Manhattan Distance: ") # printing the sum
print(distancesum(a, b, n)) # ^



# A class to represent a Point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # A utility function to find the distance between points



def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))



# A Brute Force method to return the
# smallest distance between two points

def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val


# function to find the
# distance between the closest points of
# strip of given size.
def stripClosest(strip, size, d):
    # Initialize the minimum distance as d
    min_val = d

    strip.sort(key=lambda point: point.y)



    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val


# A recursive function to find the smallest distance

def closestUtil(P, n):
    # If there are 2 or 3 points,
    # then use brute force
    if n <= 3:
        return bruteForce(P, n)

        # Find the middle point
    mid = n // 2
    midPoint = P[mid]

    dl = closestUtil(P[:mid], mid)
    dr = closestUtil(P[mid:], n - mid)

    # Find the smaller of two distances
    d = min(dl, dr)

    # Build an array strip[]
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])

            # Find the closest points in strip.

    return min(d, stripClosest(strip, len(strip), d))


# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()
def closest(P, n):
    P.sort(key=lambda point: point.x)

    # Use recursive function closestUtil() to find the smallest distance
    return closestUtil(P, n)


# Driver code (idk if im saying that right, i think its called driver code tho)
P = [Point(5, 2), Point(2, 8),
     Point(4, 3), Point(1, 7),
     Point(60, 3), Point(420, 10)]
n = len(P)
print("Printing The Smallest Distance: ")
print(closest(P, n))
# A divide and conquer program in Python3
# to find the smallest distance from a
# given set of points.


# A class to represent a Point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # A utility function to find the


# distance between two points +
def dist1(p1, p2):
    return math.sqrt((p1.x + p2.x) *
                     (p1.x + p2.x) +
                     (p1.y + p2.y) *
                     (p1.y + p2.y))


# A Brute Force method to return the
# largest distance between two points
# in P[] of size n
def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist1(P[i], P[j]) < min_val:
                min_val = dist1(P[i], P[j])

    return min_val


# function to find the
# distance between the closest points of
# strip of given size.
def stripLargest(strip, size, d):
    # Initialize the minimum distance as d
    min_val = d

    strip.sort(key=lambda point: point.y)

    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist1(strip[i], strip[j])
            j += 1

    return min_val


# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate
def largestUtil(P, n):
    # If there are 2 or 3 points,
    # then use brute force
    if n <= 3:
        return bruteForce(P, n)

        # Find the middle point
    mid = n // 2
    midPoint = P[mid]

    dl = largestUtil(P[:mid], mid)
    dr = largestUtil(P[mid:], n - mid)

    # Find the larger of two distances
    d = min(dl, dr)

    # Build an array strip[]
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])

            # Find the largest points in strip.

    return min(d, stripLargest(strip, len(strip), d))


# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()
def largest(P, n):
    P.sort(key=lambda point: point.x)

    # Use recursive function closestUtil() to find the smallest distance
    return largestUtil(P, n)


# Driver code (idk if im saying that right, i think its called driver code tho)
P = [Point(5, 2), Point(2, 8),
     Point(4, 3), Point(1, 7),
     Point(60, 3), Point(420, 10)]
n = len(P)
print("Printing The Largest Distance: ")
print(largest(P, n))
