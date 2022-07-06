import turtle

turtle.shape('turtle')
for _ in range(5):
    turtle.forward(100)
    turtle.right(360 / 5 * 2)

turtle.forward(100)
for _ in range(5):
    turtle.forward(100)
    turtle.right(360 / 5 * 2)


turtle.done()
