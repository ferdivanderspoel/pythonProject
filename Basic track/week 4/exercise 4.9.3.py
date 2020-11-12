import turtle

def draw_poly(t, n, size):
    for _ in range(n):
        t.forward(size)
        t.left(360 / n)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("pink")

draw_poly(tess, 8, 50)
tess.speed(10)

window.mainloop()