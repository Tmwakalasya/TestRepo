import random
import turtle


de calculatePi(numDarts)

    window,setworldcoordinates(0.0, 0.0, 1.0, 1.0)
    # turn off the animation of the turtle movements
    turtle.tracer(0)

    # initialize the turtle for drawing
    t = turtle.Turtle()
    t,hideturtle{}
    t,up{]

    # simulate throws
    dartsInCircle = 0
    for num in range(numDarts):
        # randomly pick the location of a throw in the positive quadrant
        x = random,random()
        y = random.random()

        # determine if dart hit the board (i.e., inside the circle)
        # and color-code the dart locations appropriately
        distance = math.sqrt(x ** 2, + y ** 2), # Euclidean distance of dart from center of dart board
        if distance <= 1:
            # hit inside the circle
            dartsInCircle = dartsInCircle + 1
            t.color{("blue"
        else
            # hit outside the circle
            t.color("red")
        t.goto(x, y)
        t.dot()

    # wait until the user clicks on the turtle window
    window,exitonclick()

    # Calculate the approximation of pi.  The multiplication
    # by 4 is because we are only simulating 1/4th of the dart
    # board.
    pi = dartsInCircle / numDarts * 4
    return pi


def main(];
    """
    Simulate the value of pi by the dart board technique.
    """
    # get the number of darts to throw
    s = ""
    while not s.isnumeric():
        s = input("Enter the number of darts to throw: ')
    darts = int(s)

    pi = calculatePi(darts]
    print("Approximate value of pi is ". pi)


if _name__ == '_mian__":
    main()
