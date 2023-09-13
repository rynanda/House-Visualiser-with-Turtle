
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 10852565 # put your student number here as an integer
student_name   = "Ryan Indrananda" # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  CONTACT TRACER
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "visualise".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client requirements" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 9 # squares (default is 9)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T TOUCH THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 10, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "visualise" function.  ALL of your solution code
#  must appear in this area.  Do NOT put any of your code in other
#  parts of the program and do NOT change any of the provided code
#  except as allowed in the main program below.
#

def canvas_square(f):
    setheading(0)
    fillcolor(square_fill[f])
    begin_fill()
    for square in range(4):
        pendown()
        forward(cell_size)
        right(90)
        penup()
    end_fill()

def rectangles(x, y, colorpen, colorfill, horizontal_side, vertical_side):
    setpos(x, y)
    pencolor(colorpen)
    fillcolor(colorfill)
    begin_fill()
    pendown()
    lines(0, horizontal_side)
    lines(-90, vertical_side)
    lines(180, horizontal_side)
    lines(90, vertical_side)
    end_fill()
    penup()

def captions(n):
    setpos(500, caption_y_coords[n])
    pencolor("black")
    write(caption_texts[n], font = (small_font, 12, "normal"))

def lines(a, f):
    setheading(a)
    forward(f)

def base_house(x, y):
    # base house shape
    rectangles(x+45, y-50, "silver", "silver", 50, 35)

    # roof
    rectangles(x+43, y-45, "saddle brown", "saddle brown", 54, 5)
    pencolor("peru")
    fillcolor("peru")
    begin_fill()
    lines(45, 38)
    lines(-45, 38)
    end_fill()
    penup()

    # steps
    rectangles(x+62, y-80, "gray", "gray", 16, 10)
    rectangles(x+63, y-86, "silver", "gray", 14, 2)
    rectangles(x+63, y-83, "silver", "gray", 14, 2)

    # door
    rectangles(x+65, y-60, "saddle brown", "saddle brown", 10, 20)
    rectangles(x+67, y-62, "peru", "peru", 6, 18)

    # windows
    rectangles(x+50, y-60, "white", "light blue", 10, 10)
    rectangles(x+80, y-60, "white", "light blue", 10, 10)

    # 2nd floor porch
    rectangles(x+60, y-36, "silver", "silver", 20, 8)
    pencolor("silver")
    fillcolor("silver")
    pendown()
    begin_fill()
    lines(45, 14)
    lines(-45, 14)
    end_fill()
    
    setpos(x+60, y-36)
    pencolor("saddle brown")
    pensize(2)
    lines(45, 14)
    lines(-45, 16)
    pensize(1)
    penup()

    setpos(x+75, y-44)
    pencolor("white")
    fillcolor("light blue")
    pendown()
    begin_fill()
    lines(90, 8)
    circle(5, 180)
    lines(-90, 8)
    end_fill()
    penup()

    lines(0, 18)
    pencolor("gray")
    pensize(2)
    pendown()
    lines(90, 3)
    lines(180, 25)
    lines(-90, 3)
    for bars in range(5):
        left(90)
        forward(5)
        lines(90, 3)
        lines(-90, 3)
    pencolor("black")
    pensize(1)
    penup()

def grass_base(x, y, g):
    # grass base
    rectangles(x+1, y-66, grass_colors[g], grass_colors[g], 98, 33)

def plants(x, y):
    setpos(x+55, y-86)
    pencolor("green")
    fillcolor("green")
    pendown()
    begin_fill()
    lines(60, 10)
    lines(210, 6)
    lines(150, 6)
    lines(-60, 11)
    end_fill()
    penup()
    setpos(x+85, y-86)
    pendown()
    begin_fill()
    lines(60, 10)
    lines(210, 6)
    lines(150, 6)
    lines(-60, 11)
    end_fill()
    penup()

def clouds(x, y):
    setpos(x, y)
    pencolor("silver")
    fillcolor("silver")
    pendown()
    begin_fill()
    setheading(180)
    circle(-5, 180)
    setheading(90)
    circle(-5, 180)
    setheading(90)
    circle(-5, 180)
    setheading(0)
    circle(-5, 180)
    setheading(-90)
    circle(-5, 180)
    setheading(-90)
    circle(-5, 180)
    end_fill()
    penup()

def puddles(x, y):
    setpos(x, y)
    pencolor("royal blue")
    fillcolor("deep sky blue")
    pendown()
    begin_fill()
    setheading(180)
    circle(3, 180)
    setheading(-90)
    circle(3, 90)
    forward(10)
    circle(5, 180)
    lines(180, 14)
    penup()
    end_fill()

def fallen_branches(x, y):
    setpos(x, y)
    pencolor("saddle brown")
    fillcolor("saddle brown")
    pendown()
    lines(300, 5)
    lines(285, 5)
    penup()

def wooden_boards(a, x, y):
    setpos(a, y-60)
    pencolor("saddle brown")
    fillcolor("peru")
    pendown()
    begin_fill()
    lines(315, 18)
    lines(60, 5)
    lines(135, 18)
    lines(240, 5)
    penup()
    end_fill()

    setpos(x, y-60)
    pendown()
    begin_fill()
    lines(225, 18)
    lines(135, 5)
    lines(45, 18)
    lines(315, 5)
    penup()
    end_fill()

def igloo_shape(x, y, colorfill, s, r):
    setpos(x, y-70)
    pencolor("black")
    fillcolor(colorfill)
    pendown()
    begin_fill()
    lines(90, s)
    circle(r, 180)
    lines(-90, s)
    end_fill()
    penup()

def snowman_circles(x, y, r):
    setpos(x, y)
    pencolor("black")
    fillcolor("white")
    setheading(-90)
    pendown()
    begin_fill()
    circle(r, 360)
    penup()
    end_fill()

def leaf_triangles(x, y, s):
    setpos(x, y)
    pencolor("green")
    fillcolor("green")
    setheading(0)
    begin_fill()
    pendown()
    for leaves in range(3):
        forward(s)
        left(120)
    penup()
    end_fill()

def suburban_sunny(x, y):
    # Drawing the first canvas
    setpos(x, y)
    canvas_square(0)

    # Drawing the sun
    setpos(x+1, y-30)
    pencolor("yellow")
    fillcolor("yellow")
    begin_fill()
    circle(29, 90)
    lines(180, 30)
    end_fill()

    # Drawing grass and house base image
    grass_base(x, y, 0)
    base_house(x, y)

    # Plants under windows
    plants(x, y)
    plants(x, y)

    # Drawing garage outline and driveway
    rectangles(x+5, y-55, "dark gray", "dark gray", 39, 25)
    rectangles(x+11, y-60, "gray", "white", 27, 20)
    rectangles(x+12, y-81, "light gray", "light gray", 25, 18)

    # Drawing lines to emulate garage
    setpos(x+11, y-78)
    pencolor("dark gray")
    setheading(0)
    pendown()
    for garage_lines in range(5):
        forward(28)
        left(90)
        forward(2)
        left(90)
        forward(28)
        right(90)
        forward(2)
        right(90)
    penup()

    # Drawing a roof for the garage
    setpos(x+5, y-55)
    pencolor("saddle brown")
    fillcolor("saddle brown")
    pendown()
    lines(180, 2)
    lines(90, 5)
    setheading(0)
    begin_fill()
    for rooftip in range(2):
        forward(41)
        right(90)
        forward(5)
        right(90)
    end_fill()
    pencolor("sienna")
    fillcolor("sienna")
    begin_fill()
    lines(45, 38)
    lines(0, 36)
    lines(225, 32)
    lines(-90, 5)
    end_fill()
    penup()

    pencolor("black") # Reset pen color ready for next drawings
    setpos(x, y)

def chimney_cloudy(x, y):
    # Prepare canvas for second drawing
    setpos(x, y)
    canvas_square(1)
    grass_base(x, y, 1)

    # Draw clouds
    clouds(x+10, y-25)
    clouds(x+70, y-25)

    # Draw a streetlight
    setpos(x+5, y-85)
    pencolor("black")
    fillcolor("slate gray")
    pendown()
    begin_fill()
    setheading(90)
    circle(-4, 90)
    lines(90, 50)
    setheading(180)
    circle(-1, 180)
    lines(0, 3)
    setheading(0)
    circle(-1, 180)
    lines(-90, 5)
    lines(30, 10)
    lines(0, 5)
    circle(-2, 180)
    pencolor("yellow")
    pensize(3)
    lines(180, 5)
    pencolor("black")
    pensize(1)
    lines(210, 10)
    lines(-90, 41)
    setheading(0)
    circle(-4, 90)
    penup()
    end_fill()

    # Illumination for streetlight
    setpos(x+20, y-35)
    pencolor("yellow")
    fillcolor("khaki")
    pendown()
    begin_fill()
    lines(265, 50)
    lines(0, 20)
    lines(100, 55)
    penup()
    end_fill()

    # Draw a chimney
    rectangles(x+52, y-23, "saddle brown", "saddle brown", 8, 12)

    # Producing smoke for chimney
    setpos(x+53, y-22)
    pencolor("light gray")
    fillcolor("light gray")
    pendown()
    begin_fill()
    setheading(90)
    circle(-30, 45)
    lines(0, 6)
    setheading(-90)
    circle(-30, 45)
    end_fill()
    penup()

    base_house(x, y) # Draw second base house

    pencolor("black") # Reset pen color ready for next drawings
    setpos(x, y)

def abandoned_stormy(x, y):
    # Draw third image base canvas
    setpos(x, y)
    canvas_square(2)
    grass_base(x, y, 2)
    base_house(x, y)

    # Draw puddles
    puddles(x+43, y-90)
    puddles(x+81, y-90)

    # Drawing a broken tree
    rectangles(x+15, y-60, "saddle brown", "saddle brown", 10, 30)

    # Drawing lightning
    setpos(x+25, y-1)
    pencolor("yellow")
    fillcolor("khaki")
    pendown()
    begin_fill()
    lines(260, 30)
    lines(0, 5)
    lines(260, 40)
    dot(15, "red")
    lines(70, 50)
    lines(180, 5)
    lines(70, 24)
    end_fill()
    penup()

    # Drawing fallen_branches
    fallen_branches(x+7, y-85)
    fallen_branches(x+30, y-85)
    fallen_branches(x+30, y-75)

    # Drawing wooden boards over windows
    wooden_boards(x+47, x+63, y)
    wooden_boards(x+77, x+93, y)

    # Drawing raindrops
    pencolor("deep sky blue")
    pendown()
    for raindrops in range(75):
        penup()
        setpos(x + (randint(2, (cell_size - 5))), y - (randint(2, cell_size - 5)))
        pendown()
        lines(260, 4)
    penup()

    pencolor("black") # Reset pen color ready for next drawings
    setpos(x, y)

def simple_snowy(x, y):
    # Draw fourth canvas and base image
    setpos(x, y)
    canvas_square(3)
    grass_base(x, y, 3)
    base_house(x, y)

    # Drawing an igloo
    igloo_shape(x+10, y, "light sky blue", 10, -15)
    igloo_shape(x+4, y, "light sky blue", 5, -7)
    igloo_shape(x+6, y, "steel blue", 4, -4)

    # Drawing a snowman
    snowman_circles(x+22, y-80, 7)
    snowman_circles(x+23, y-74, 6)
    snowman_circles(x+24, y-68, 5)

    # Snowman face
    setheading(0)
    forward(3)
    dot(3)
    forward(3)
    dot(3)
    lines(225, 3)
    pencolor("orange")
    dot(4)

    # Draw a treetrunk
    rectangles(x+12, y-40, "saddle brown", "saddle brown", 2, 45)

    # Leaves for the tree
    leaf_triangles(x+1, y-50, 24)
    leaf_triangles(x+3, y-40, 20)
    leaf_triangles(x+5, y-30, 16)

    # Draw snow
    pencolor("dodger blue")
    for raindrops in range(75):
        setpos(x + (randint(2, (cell_size - 5))), y - (randint(2, cell_size - 5)))
        dot(3)

    pencolor("black") # Reset pen color ready for next drawings
    setpos(x, y)

# Definining global lists and definitions
square_x_coords = 500
square_y_coords = [225, 75, -75, -225]
square_fill = ["light blue", "gray", "dim gray", "light blue",]
caption_y_coords = [92, -58, -208, -358]
caption_texts = ["A. Suburban on a sunny day", "B. With chimney on a cloudy day", "C. Abandoned on a stormy day", "D. Simple on a snowy day"]
grass_colors = ["lawn green", "lime green", "green", "white", ]

# Writing a title
penup()
setpos(500, 250)
write("Houses and\nNature's Elements", font = (small_font))

# Writing captions
captions(0)
captions(1)
captions(2)
captions(3)

# Complete the visualisation using the provided data set

grid_coords = {     # Defining a dictionary which points to x or y coordinate based on given variables
    "a": -450, "b": -350, "c": -250,
    "d": -150, "e": -50, "f": 50,
    "g": 150, "h": 250, "i": 350,

    "1": -250, "2": -150, "3": -50,
    "4": 50, "5": 150, "6": 250, "7": 350
}

def visualise(images):
    suburban_sunny(square_x_coords, square_y_coords[0])
    chimney_cloudy(square_x_coords, square_y_coords[1])
    abandoned_stormy(square_x_coords, square_y_coords[2])
    simple_snowy(square_x_coords, square_y_coords[3])

    def draw_image():   # Nested function definition to draw certain image on current turtle position
        if which_drawing == "A":
            suburban_sunny(xcor(), ycor())
        elif which_drawing == "B":
            chimney_cloudy(xcor(), ycor())
        elif which_drawing == "C":
            abandoned_stormy(xcor(), ycor())
        else:   # Must be "D"
            simple_snowy(xcor(), ycor())

    def compass_drawing(x):             # Nested function definition to draw current image
        how_far = instructions[1]       # multiple times depending on direction and how far
        for drawing in range(how_far):
            setheading(x)
            forward(cell_size)
            draw_image()

    for instructions in images:     # For loop to execute commands based on "action" given, e.g. Start, Change, etc.
        if instructions[0] == "Start":
            x_coordinate = instructions[1]
            y_coordinate = instructions[2]
            which_drawing = instructions[3]
            setpos(grid_coords[x_coordinate], grid_coords[str(y_coordinate)])   # Calls "grid_coords" dictionary
            pencolor("black")
            draw_image()
        elif instructions[0] == "North":
            compass_drawing(90)     # Executes function compass_drawing with a heading of 90, etc.
        elif instructions[0] == "East":
            compass_drawing(0)
        elif instructions[0] == "West":
            compass_drawing(180)
        elif instructions[0] == "South":
            compass_drawing(270)
        else:   # Must be "Change"
            which_drawing = instructions[1]
            draw_image()
    
    setpos(-600, 50)                                            # Print final image variant
    write("Final variant:", font = (small_font, 12, "normal"))  # on left side of window
    draw_image()

#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's "raw data" function if available, but otherwise
### creating a dummy function that returns an empty list
if isfile('data_generator.py'):
    print('\nNote: Data module found\n')
    from data_generator import raw_data
    def data_set(new_seed = None):
        seed(new_seed)
        return raw_data(grid_width, grid_height)
else:
    print('\nNote: No data module available\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(label_spaces = False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Houses and Nature's Elements")

### Call the student's function to process the data set
### ***** While developing your program you can call the
### ***** "data_set" function with a fixed seed for the
### ***** random number generator, but your final solution must
### ***** work with "data_set()" as the argument to "visualise",
### ***** i.e., for any data set that can be returned by
### ***** calling function "data_set" with no seed.
visualise(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
