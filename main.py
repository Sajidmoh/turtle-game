import turtle
import random

score = 105
t = turtle.Turtle()
t.color("black")

obstacle = turtle.Turtle()
obstacle.shape("square")
obstacle.color("red")

obstacle.up()
obstacle.forward(100)
obstacle.left(90)
obstacle.forward(100)


obstacle2 = turtle.Turtle()
obstacle2.shape("square")
obstacle2.color("red")
obstacle2.up()


obstacle2.left(90)
obstacle2.forward(50)
obstacle2.right(90)
obstacle2.forward(50)

obstacle3 = turtle.Turtle()
obstacle3.shape("square")
obstacle3.color("red")
obstacle3.up()

obstacle3.left(90)
obstacle3.forward(120)

obstacle4 = turtle.Turtle()
obstacle4.shape("square")
obstacle4.color("red")
obstacle4.up()

obstacle4.forward(100)
obstacle4.goto(-50, 90)


finish = turtle.Turtle()
finish.color("green")
finish.shape("circle")
finish.up()
finish.goto(100, 150)


def win():
    if t.distance(finish) < 20:
        print("YOu win .. and you are amzing")
        return True


def collision():
    if t.distance(obstacle) < 20:
        return True
    elif t.distance(obstacle2) < 20:
        return True
    elif t.distance(obstacle3) < 20:
        return True
    elif t.distance(obstacle4) < 20:
        return True


# for i in range(10):
#     t.forward(100)
#     type.right(90)

# controls

# list of obstacles

obstacles = [obstacle, obstacle2, obstacle3, obstacle4]


def movingObstacle(move):
    if move % 2 == 0:
        for i in obstacles:
            angle = random.randint(0, 360)
            displacement = random.randint(-60, 60)
            i.right(angle)
            i.forward(displacement)
            if i.position()[0] > 200 or i.position()[0] < -200:
                i.goto(0, 0)

    else:
        obstacle2.backward(100)


move = 0

while True:
    print("a - left  , w - forward , s - backwards, d - right,  q - quit")

    control = input("Enter :")

    if control == "w":
        t.forward(50)

    elif control == "a":
        t.left(90)

    elif control == "q":
        break
    elif control == "s":
        t.forward(-50)
    elif control == "d":
        t.right(90)

    movingObstacle(move)

    if collision():
        print("You lose ")
        break

    if win():
        print("Your score was: ",score)
        break

    move += 1
    score -= 1