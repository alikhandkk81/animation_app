import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)


def turtle(lenth, angle):
  for i in range(4):
    my_turtle.forward(lenth)
    my_turtle.left(angle)
    

    
for i in range(100):
    turtle(100, 90)
    my_turtle.right(11)
