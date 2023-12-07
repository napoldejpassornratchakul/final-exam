import turtle
import random

class Polygon:
    def __init__(self,num_sides, size, orientation, location , color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))






# def draw_polygon(num_sides, size, orientation, location, color, border_size):
#     turtle.penup()
#     turtle.goto(location[0], location[1])
#     turtle.setheading(orientation)
#     turtle.color(color)
#     turtle.pensize(border_size)
#     turtle.pendown()
#     for _ in range(num_sides):
#         turtle.forward(size)
#         turtle.left(360/num_sides)
#     turtle.penup()



turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
border_size = random.randint(1, 10)
p1 = Polygon(num_sides, size, orientation, location, color , border_size)
p1.draw_polygon()


# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original
p2 = Polygon(num_sides, size, orientation, location, color , border_size)
p2.draw_polygon()


# draw_polygon(num_sides, size, orientation, location, color, border_size)
num_input = int(input())
if num_input == 1:
    for i in range(20):
        num_sides = 3
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        p1 = Polygon(num_sides, size, orientation, location, color, border_size)
        p1.draw_polygon()

if num_input == 2:
    for i in range(20):
        num_sides = 4
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        p1 = Polygon(num_sides, size, orientation, location, color, border_size)
        p1.draw_polygon()

if num_input == 3:
    for i in range(20):
        num_sides = 5
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        p1 = Polygon(num_sides, size, orientation, location, color, border_size)
        p1.draw_polygon()

if num_input == 4:
    for i in range(20):
        num_sides = random.randint(3,5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        p1 = Polygon(num_sides, size, orientation, location, color, border_size)
        p1.draw_polygon()

if num_input == 5:
    for i in range(20):
        num_sides = 3
        size = random.randint(50, 150)
        orientation = random.randint(0, 45)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        p1 = Polygon(num_sides, size, orientation, location, color, border_size)
        p1.draw_polygon()



# hold the window; close it by clicking the window close 'x' mark
turtle.done()