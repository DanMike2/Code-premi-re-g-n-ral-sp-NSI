import turtle, random, colorsys

t = turtle.Turtle()
t.speed(100)
t.shape("turtle")

screen = turtle.Screen()
screen.bgcolor("antique white")


# Pot
color = random.random(), random.random(), random.random()

def carre(cote):
    t.begin_fill()
    for i in range(4):
        t.forward(cote)
        t.right(90)
    t.end_fill()


def boué():
    t.pencolor("black")
    t.fillcolor(color)
    t.begin_fill()
    t.forward(100)
    t.left(180)
    t.circle(20,-180)
    t.left(180)
    t.forward(200)
    t.left(180)
    t.circle(20,-180)
    t.right(180)
    t.forward(100)
    t.end_fill()
    t.color(color)
    t.up()
    t.forward(50)
    t.down()
    carre(40)
    t.up()
    t.left(180)
    t.forward(125)
    t.right(180)
    t.down()
    carre(40)
    t.up()
    t.forward(75)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.down()

def pot():
    t.pensize(3)
    for i in range(5):
        boué()
    t.color("black")
    t.forward(100)
    t.back(200)
    t.up()
    t.home()
    t.down()
    t.forward(100)
    t.back(200)
    t.home()
# ...............................................................................................................................

# Fleur 1
def dessin_fleur_A(t):
    # Tige
    t.pensize(5)
    t.color("green")
    t.forward(60)

    # Feuille
    t.begin_fill()
    for i in range (2):
        t.circle(50, 90)
        t.left(90)
    t.end_fill()
    t.forward(80)
    t.up()
    t.forward(30)
    t.down()

    # Centre de la fleur
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.down()
    t.pensize(1)
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()
    t.circle(30, 360)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(30)
    t.left(90)
    t.left(180)
    t.down()

    # Graines au centre de la fleur
    t.color("maroon")
    for i in range(60):
        t.up()
        t.setheading(i * 137.5)
        t.forward(i * 0.5)
        t.dot(3)
        t.backward(i * 0.5)

    # Pétales
    petal_colors = ["gold", "orange", "goldenrod"]
    t.color("orange")
    for i in range(18):
        t.up()
        t.setheading(90)
        t.left(20 * i)
        t.forward(25)
        t.down() 
        color2 = petal_colors[i % 3]
        t.fillcolor(color2)
        t.begin_fill()
        for j in range(2):
            t.circle(42, 80)
            t.left(100)
        t.up()
        t.back(25)
        t.down()
        t.end_fill()

# Fleur 2
def dessin_fleur_B(t):
# Tige
    t.pensize(5)
    t.color("green")
    t.forward(120)
    t.back(30)
    t.pensize(2)

    t.up()
    t.left(90)
    t.back(5)
    t.right(90)
    t.down()
# Fleur
# Pétales arrière-plans
    for i in range(36):
        t.color("medium violet red")
        t.circle(120, 60)
        t.left(170)

#  Pétales plan moyen
    t.forward(10)
    for i in range(36):
        t.color("deep pink")
        t.circle(100, 60)
        t.left(170)

# Pétales premier-plan
    t.forward(10)
    for i in range(36):
        t.color("hot pink")
        t.circle(80, 60)
        t.left(170)


# Fleur 3
def dessin_fleur_C(t):
    # Tige
    t.pensize(5)
    t.color("green")
    t.forward(100)
    t.up()
    t.forward(60)
    t.down()
    t.pensize(1)

    # Fleur
    turtle.tracer(30)
    h = 0
    for i in range(1300):
        h += 0.0008
        r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(r, g, b)
        if i % 5 == 0:
            t.right(3)
        t.forward(40)
        t.right(360/5)


# Fleur 4
def dessin_fleur_D(t):

    # Tige
    t.color("green")
    t.pensize(5)
    t.forward(180)
    t.pensize(1)

    # Fleur
    for i in range(20):
        if i % 3 == 0:
            t.color(random.random(), random.random(), random.random())
        elif i % 3 == 1:
            t.color(random.random(), random.random(), random.random())
        else:
            t.color(random.random(), random.random(), random.random())
        
        t.begin_fill()
        t.circle(50, 60)
        t.left(120)
        t.circle(50, 60)
        t.end_fill()
        t.left(190)


def dessin_fleur_E(t):
    # Tige
    t.pensize(5)
    t.color("green")
    t.forward(130)
    t.pensize(1)

    # Fleur
    for cote in [40,30,20]:
        for i in range(24):
            t.fillcolor(random.random(), random.random(), random.random())
            carre(cote)
            t.right(15)


def dessin_fleur_F(t):
    color = random.random(), random.random(), random.random()
    # Tige
    t.color("green")
    t.pensize(5)
    t.forward(120)
    t.up()
    t.forward(70)
    t.down()
    t.pensize(1)

    # Fleur
    t.pencolor(color)
    t.right(135)
    for i in range(48):
        t.pencolor(color)
        t.circle(35,180)
        t.circle(35,180)
        t.left(7.5)

def dessin_fleur_G(t):
    # tige
    t.pensize(5)
    t.pencolor("green")
    t.forward(160)
    t.pensize(1)

    # Fleur
    def petal(t, size):
        color = random.random(), random.random(), random.random()
        t.fillcolor(color)
        t.pencolor(color)
        t.begin_fill()
        for i in range(2):
            t.circle(size, 60)
            t.left(120)
        t.end_fill()


    def draw_flower(t, number_of_petals, petal_size):
        for i in range(number_of_petals):
            petal(t, petal_size)
            t.left(360 / number_of_petals)


    def fractal(t, number_of_petals, initial_petal_size, layers=4):
        for layer in range(layers):
            size = initial_petal_size * (0.75 ** layer)


            draw_flower(t, number_of_petals, size)


    dessin_Fleur_G = fractal(t, number_of_petals=36, initial_petal_size = 70, layers=3)


# Appel de la fonction du pot
pot()

# Choix des fleur
types = ["A", "B", "C", "D", "E", "F", "G"]
fleurs = random.sample(types, 3)

# Choix de l'angle
angles = random.sample([45, 90, 135], 3)

# Dessiner la fleur en partant de home
for typ, ang in zip(fleurs, angles):
    t.up()
    t.home()
    t.down()
    t.setheading(ang)
# Appel des fonctions de fleurs
    if typ == "A":
        dessin_fleur_A(t)
    elif typ == "B":
        dessin_fleur_B(t)
    elif typ == "C":
        dessin_fleur_C(t)
    elif typ == "D":
        dessin_fleur_D(t)
    elif typ == "E":
        dessin_fleur_E(t)
    elif typ == "F":
        dessin_fleur_F(t)
    elif typ == "G":
        dessin_fleur_G(t)

t.color("black")
t.up()
t.goto(150, -200)
t.down()
t.write("Gabriel Fortin Huet", align = "left", font = ("Arial", 12, "italic"))
t.up()
t.goto(210, -220)
t.down()
t.write("&", align = "left", font = ("Arial", 12, "italic"))
t.up()
t.goto(150, -240)
t.down()
t.write("Raphaël Roquigny", align = "left", font = ("Arial", 12, "italic"))
t.up()
t.goto(200, -260)
t.down()
t.write("1G4", align = "left", font = ("Arial", 12, "italic"))



t.hideturtle()
turtle.done()
