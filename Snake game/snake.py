from turtle import Turtle, left

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_position = [(0,0), (-20, 0), (-40, 0)]
        self.segments = []
        self.snake_body()
        self.head = self.segments[0]

    def snake_body(self):
        for position in self.all_position:
            self.new_segmnet(position)

    def new_segmnet(self, position):
        s_snake = Turtle("square")
        s_snake.penup()
        s_snake.color("white")
        s_snake.goto(position)
        self.segments.append(s_snake)

    
    def extend(self):
        self.new_segmnet(self.segments[-1].position())
    

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.snake_body()
        self.head = self.segments[0]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        
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