import turtle
import math

wn=turtle.Screen()
wn.bgpic("Background.png")
wn.title("A Maze Game")
wn.setup(700,700)
wn.tracer(0)

#set score on a screen
score=turtle.Turtle(visible=False)  # For time output
score.penup()
score.setposition(300, 300)  # In this position I want to output variable
score.write("Points="+str(0),align="right",font=("Arial",14,"normal"))


#register shapes
turtle.register_shape("wall.gif")
turtle.register_shape("Player.gif")
turtle.register_shape("Candy.gif")
turtle.register_shape("Pumbkin.gif")
turtle.register_shape("Witch.gif")
turtle.register_shape("Door.gif")

#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
#create Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Player.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        #calculate the spot to move to
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        #check if the space has a wall
        if (move_to_x , move_to_y) not in walls:
            if (move_to_x , move_to_y) not in dr:
                    self.goto(move_to_x , move_to_y)
            
    def go_down(self):
        #calculate the spot to move to
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        #check if the space has a wall
        if (move_to_x , move_to_y) not in walls:
            if (move_to_x , move_to_y) not in dr:
                    self.goto(move_to_x , move_to_y)
            
    def go_left(self):
        #calculate the spot to move to
        move_to_x=player.xcor()-24
        move_to_y=player.ycor()
        #check if the space has a wall
        if (move_to_x , move_to_y) not in walls:
            if (move_to_x , move_to_y) not in dr:
                    self.goto(move_to_x , move_to_y)
           
    def go_right(self):
        #calculate the spot to move to
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        #check if the space has a wall
        if (move_to_x , move_to_y) not in walls:
            if (move_to_x , move_to_y) not in dr:
                    self.goto(move_to_x , move_to_y)

    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance < 5 :
            return True
        else:
            return False

    def is_collide(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance < 25 :
            return True
        else:
            return False
        
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("Candy.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
        
class Obstacle(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("Pumbkin.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        
class Door(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("Door.gif")
        self.color("brown")
        self.penup()
        self.speed(0)
        #self.gold=100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
    
#create levels lists
levels=[""]

#define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX             TX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X   T   XX  XXX        XX",
"XXXXXX  XX  XXX     O  XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXXT XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X        XXXXXXXXXXXXXXX",
"XT   O           XXXXXXXX",
"XXXXXXXXXXXX     XXXXX TX",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                  O  X",
"XXX O   T   XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX             TD",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XXT         XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"]
#add a treasure list
treasures= []

#add a door list
doors=[]

#add a obstacle list
obstacles=[]

#add maze to mazes lists
levels.append(level_1)

#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get the character at each x,y coordinate
            #note te order of each y and xin the next line
            character=level[y][x]
            #calculate the screen x,y coordinate
            screen_x=-288+(x*24)
            screen_y=288-(y*24)

            #check if it is an X (representing a wall)
            if character=='X':
                pen.goto(screen_x,screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                
                #add cordinates to wall list
                walls.append((screen_x,screen_y))

            #check if it is a P (representing the player)
            if character=="P":
                player.goto(screen_x,screen_y)

            #check if it is a T(representing treasure)
            if character=="T":
                treasures.append(Treasure(screen_x,screen_y))

            #check if it is a O(representing obstacle)
            if character=="O":
                obstacles.append(Obstacle(screen_x,screen_y))
                pen.stamp()

                #add co-ordinates to obst list
                obst.append((screen_x,screen_y))

            #check if it is a O(representing obstacle)
            if character=="D":
                doors.append(Door(screen_x,screen_y))
                pen.stamp()

                #add co-ordinates to obst list
                dr.append((screen_x,screen_y))

#create class instances
pen=Pen()
player=Player()


#create walls co-ordinate lists
walls=[]

#create obst co-ordinate lists
obst=[]

#create door co-ordinate lists
dr=[]

#set up the level
setup_maze(levels[1])

#keyboard bindings
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

#wn.tracer(0)

#Main Game Loop

while True :
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold : {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
            score.undo()  # undraw the last time update
            score.setposition(300,300)
            score.write("Points : {}".format(player.gold),align="right",font=("Arial",14,"normal"))
            #str(t))  # Show the time variable  on screen
            wn.update()
    for obstacle in obstacles:
        if player.is_collision(obstacle):
            print("score detucted")
            player.gold-=50
            print("Points : {}".format(player.gold))
            player.setpos((-264,264))
            score.undo()  # undraw the last time update
            score.setposition(300,300)
            score.write("Points: {}".format(player.gold),align="right",font=("Arial",14,"normal"))
            
    for door in doors:
        if player.gold >= 300:
            door.hideturtle()
            if player.is_collide(door):
                print("LEVEL 3")
                wn.clear()
                import Title3
            
        
    wn.update()

















    
