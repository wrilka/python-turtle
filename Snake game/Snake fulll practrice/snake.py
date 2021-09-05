from turtle import Turtle

ALL_POSITON = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_segment()
        self.head = self.segments[0]

    
    def snake_segment(self):
        for position in ALL_POSITON:
            self.add_segment(position)
        
    def add_segment(self, position):
        s_segment = Turtle("square")
        s_segment.speed(0)
        s_segment.color("white")
        s_segment.penup()
        s_segment.goto(position)
        self.segments.append(s_segment)
    
    def extend_segment(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for segment in range(len(self.segments) -1, 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)