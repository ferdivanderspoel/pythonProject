import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
fer = turtle.Turtle()
fer.pensize(3)
fer.color("pink")

def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(360 / n)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

draw_equitriangle(fer, 100)

window.mainloop()