from turtle import Turtle

CPU_POSITIONS = [(350,-20), (350,0), (350,20)]
MOVE_DISTANCE = 1


class CPU_Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.hideturtle()
        self.createpaddle()
        self.leadsegment = self.segments[0]

    def createpaddle(self):
        for position in CPU_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("slow")
        new_segment.setheading(90)
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def move_forward(self):
        #for segment in range(len(self.segments) -1 , 0, -1):
           # new_x = self.segments[segment - 1].xcor()
           # new_y = self.segments[segment - 1].ycor()
           # self.segments[segment].goto(x=new_x, y=new_y)
        #self.leadsegment.forward(MOVE_DISTANCE)
        for segment in self.segments:
             segment.forward(5)

    def reverse_paddle(self):
        if self.leadsegment.ycor() > 220:
            for segment in self.segments:
                segment.setheading(270)
        if self.leadsegment.ycor() < -280:
            for segment in self.segments:
                segment.setheading(90)






