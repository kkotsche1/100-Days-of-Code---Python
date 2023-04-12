from turtle import Turtle 

USER_POSITIONS = [(-350,20), (-350,0), (-350,-20)]
MOVE_DISTANCE = 1


class Paddle(Turtle):
   
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.segments = []
        self.createpaddle()
        self.lead_segment = self.segments[0]
    
    
    def createpaddle(self):
        for position in USER_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setheading(90)
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def reverse_paddle(self):
        if self.lead_segment.ycor() > 220:
            for segment in self.segments:
                segment.setheading(270)
        if self.lead_segment.ycor() < -280:
            for segment in self.segments:
                segment.setheading(90)

    
    def move_forward(self):
        # for segment in range(len(self.segments) - 1, 0, -1):
        #     new_x = self.segments[segment - 1].xcor()
        #     new_y = self.segments[segment - 1].ycor()
        #     self.segments[segment].goto(x=new_x, y=new_y)
        # self.lead_segment.forward(MOVE_DISTANCE)
        for segment in self.segments:
             segment.forward(5)

    def up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(10)

    def down(self):
        for segment in self.segments:
            segment.setheading(270)
            segment.forward(10)