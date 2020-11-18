class Point (object) : #class == create objects
    """Represents a point in 2-D space."""

#print (Point)

#blank = Point ()

#blank.x = 3.0
#blank.y = 4.0

#import math
#print ('(%g, %g)' % (blank.x, blank.y))
#distance = math.sqrt (blank.x**2 + blank.y**2)
#print (distance)

def print_point (p) :
    print ('(%g, %g)' % (p.x, p.y))

def distance_between_points () :
    a = Point ()
    b = Point ()
    a.x = int (input ('enter x coordinate of a\n'))
    b.x = int (input ('enter x coordinate of b\n'))
    a.y = int (input ('enter y coordinate of a\n'))
    b.y = int (input ('enter y coordinate of b\n'))
    c = math.sqrt ( (a.x-b.x)**2 + (a.y-b.y)**2 )
    print (c)

class Rectangle (object) :
    """Represent a rectangle.

       attributes: width, height, corner,
       """

box = Rectangle ()
box.width = 100.0
box.height = 200.0
box.corner = Point ()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center (rect) :
    p = Point ()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

def grow_rectangle (rect, dwidth, dheight) :
    rect.width += dwidth
    rect.height += dheight

class Time (object) :
    """Represents the time of the day.
    attributes: hour, minute, second
    """

time = Time ()
time.hour = 11
time.minute = 59
time.second = 30

def print_time (time) :
    print ('(%.2d: %.2d: %.2d)' % (time.hour, time.minute, time.second))

t1 = Time ()
t1.hour = 11
t1.minute = 30
t1.second = 00
print_time (t1)

t2 = Time ()
t2.hour = 10
t2.minute = 45
t2.second = 00
print_time (t2)

def is_after (t1, t2) :   
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

