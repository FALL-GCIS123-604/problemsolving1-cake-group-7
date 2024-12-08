"""Group Members: Thamanna Mohan (UID: 401009752), Sannyukta Navsarikar (UID: 412001768), Azeem Ali (UID: 744003916), Loretta Denis (UID: 764002677)"""

import turtle



def frosting(x,y,thick,top,r,color):
    """top is the upper line"""
    """ thick is how much the turtle goes before it starts curving and then after curving to meet the top line """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(top)
    turtle.right(90)
    turtle.forward(thick)
    turtle.circle(r,180)
    turtle.right(180)
    turtle.circle(r,180)
    turtle.right(180)
    turtle.circle(r,180)
    turtle.forward(thick)
    turtle.end_fill() 


def table(v,f,c):
    """to draw the tabletop """
    def trapezium(l,b,c,x,y):
        turtle.pencolor(c)
        turtle.fillcolor(c)
        turtle.begin_fill()
        turtle.goto(x,y)
        turtle.penup()
        turtle.left(180)
        turtle.forward(l/2)
        turtle.left(180)
        turtle.pendown()
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(b)
        turtle.left(60)
        """ to know the x co-ordinate of 1st point"""
        a = turtle.xcor()
        turtle.penup()
        turtle.goto(0,0)
        turtle.forward(l/2)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(b)
        turtle.right(60)
        """ to know the x co-ordinate of 2nd point"""
        b = turtle.xcor()
        d = turtle.ycor()
        if a < 0 and b > 0:
            c = b-a
        elif b < 0 and a > 0:
            c = a-b
        else:
            c = -(b-a)
        turtle.forward(c)
        turtle.end_fill()
        return b,d
        
        

    """ to draw the table legs on right"""
    def verticalrightrectangles(l,b,c):
        turtle.pencolor(c)
        turtle.fillcolor(c)
        turtle.begin_fill()
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(l)
        turtle.end_fill()

    """  to draw the table legs on left"""
    def verticalleftrectangles(l,b,c):
        turtle.pencolor(c)
        turtle.fillcolor(c)
        turtle.begin_fill()
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)
        turtle.forward(l)
        turtle.end_fill()

    def tablecom(l,b,c,x=0,y=0):
        """to draw the top of the table"""
        t,u = trapezium(l,b,c,x,y)
        turtle.right(90)
        verticalrightrectangles(l/2,b/3,c)
        turtle.left(90)
        turtle.penup()
        turtle.forward(2*b/3)
        turtle.pendown()
        turtle.right(270)
        verticalrightrectangles(l/3,b/3,c)
        turtle.penup()
        turtle.goto(t,u)
        turtle.left(180)
        turtle.pendown()
        verticalleftrectangles(l/2,b/3,c)
        turtle.right(90)
        turtle.penup()
        turtle.forward(2*b/3)
        turtle.pendown()
        turtle.left(270)
        verticalleftrectangles(l/3,b/3,c)
        turtle.right(90)
        turtle.left(180)

    tablecom(v,f,c)


""" making a cake  """
def make_cake(flavour_ch, size,v,f, co):
    """to draw cake """

    i = 0
    
    """to choose the colour by assigning hex code to flavour"""
    match(flavour_ch):
        

        case "chocolate" : color_list =  ['#352728', '#7c665f', '#4e3c3b']
        case "vanilla" : color_list =  ['#CB8944', '#F3E5AB', '#FFFAE3']
        case "strawberry" : color_list = ['#f0e1ba', '#f07173', '#f6ced5']
        case "vanilla" : color_list = ['#CB8944', '#F3E5AB', '#FFFAE3']
        case "shrek" : color_list = ['#b0c400', '#d5de2e', '#c3bc95']
    
    """Initializing values """
    x, y = 0, 0
    
    """Finilizing hex color list based on parameter"""
    forward_length, u_length = v/3, f

    def cake_time(i, x, y, forward_length):
        """to draw 1 layer of the cake """
        
        turtle.penup()
        turtle.goto(x, y) #setting turtles position

        turtle.color(color_list[i - 3])
        turtle.begin_fill()
        turtle.pendown()
        turtle.forward(forward_length/2)
        turtle.right(180)
        turtle.forward(forward_length)
        turtle.left(90)
        turtle.forward(u_length)
        turtle.left(90)
        turtle.forward(forward_length)
        xo = turtle.xcor()
        yo = turtle.ycor()
        turtle.left(90)
        turtle.forward(u_length)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0,y)
        turtle.left(90)
        turtle.forward(u_length)
        lo= turtle.xcor()
        vo =turtle.ycor()
        turtle.left(90)
        turtle.left(180)
        frosting(xo,yo,f/4,0,forward_length/6,co)
        turtle.left(90)
        turtle.goto(lo,vo)
            

        x = 0 
        y = u_length*(i+1)
        forward_length = forward_length / (4/3)

        return x, y, forward_length

    """assigning attributes to make layers of the cake """
    x, y, forward_length = cake_time(0, x, y, forward_length)
    x, y, forward_length = cake_time(1, x, y, forward_length)
    x, y, forward_length = cake_time(2, x, y, forward_length)
    turtle.left(180)

        

    





"""to draw a candle"""
def candle(colour,f):

    turtle.pensize(5)
    turtle.pendown()
    k = turtle.ycor()
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(f/8)
    turtle.left(180)
    turtle.forward(f/4)
    turtle.left(90)
    turtle.forward(f)
    turtle.left(90)
    turtle.forward(f/4)
    turtle.left(90)
    turtle.forward(f)
    turtle.end_fill()
    turtle.goto(0,k)
    turtle.penup()
    turtle.goto(0,k+f)
    turtle.pendown()
    turtle.left(180)
    turtle.pencolor("orange")
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.forward(f/4)
    turtle.end_fill()


def validator(v, f, flavour):
    """validating the values that is given by the user"""

    if not(v.isdigit()) or not(f.isdigit()):
        print("""
        ERROR: MAKE SURE THE VALUES FOR LENGTH OR BREADTH
        ARE IN NUMBERICALS
        """)
        return 0
    

    if int(f) >= int(v)/2:
        print("""
        BREADTH MUST BE LESS THAN HALF OF LENGTH
        """)
        return 0

    if flavour.lower() not in ['chocolate', 'strawberry', 'vanilla', 'shrek']:
        print("Sorry we don't have the flavour available yet :(")
        return 0
    
    return 1

def write(v):
    #to write happy birthday 

    turtle.penup()
    pos = turtle.pos()
    turtle.goto(pos[0] - (100 * v/600), pos[1])
    f_size = int(50 * v/600) // 2
    turtle.write("HAPPY BIRTHDAY !!", font=('Great Vibes', f_size, "normal"))

def main():
    """to execute the entire code with output"""


    s = """
==============================
WELCOME TO MAKE A CAKE CONSOLE
==============================
        """


    print(s)
    v = input("Enter table length:- ")
    f = input("Enter table breadth:- ")
    c = input("Enter colour of table:- ")
    colour=input("Enter colour of candle ")
    co = input("Enter colour of frosting:- ")

    print("""
        ===========
        FLAVOURS :0
        ===========
        
        ++++++++++++
        CHOCOLATE <3
        STRAWBERRY :)
        VANILLA :P
        SHREK :3
        ++++++++++++
        """)

    flavour = input("Enter your flvaor choice: ")
    check = validator(v, f, flavour)

    if check == 1:
        v, f = int(v), int(f)
        Screen = turtle.Screen()
        Screen.setup(width=(v*1.2), height=(f + 600))
        table(v,f,c)
        make_cake(flavour, 3,v,f, co)
        candle(colour, f)
        write(v)
        turtle.speed(1000)
        input("")
    
    else:
        print("""
++++++++++++++
RESTARTING....
++++++++++++++
              """)
        main()


main()