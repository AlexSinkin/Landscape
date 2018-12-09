import graphics as gr


def draw_tree():
    # Ствол, хвоя (3 уровня)
    draw_trunk(790, 380)

    for n in range(3):
        draw_needles(710, 300 - n * 50)


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 250))
    sky.setFill('blue')
    sky.draw(window)


def draw_sun(x, y):
    sun = gr.Circle(gr.Point(x, y), 50)
    sun.setFill('yellow')
    sun.setOutline('yellow')
    sun.draw(window)
    return sun


def draw_ground():
    ground = gr.Rectangle(gr.Point(0, 250), gr.Point(1000, 500))
    ground.draw(window)
    ground.setFill('dark grey')


def draw_clouds():
    clouds_coords = [(90, 75), (120, 75),
                     (75, 100), (105, 100), (135, 100),
                     (590, 95), (620, 95),
                     (575, 120), (605, 120), (635, 120),
                     (790, 105), (820, 105),
                     (745, 130), (775, 130), (805, 130)]

    for coords in clouds_coords:
        cloud = gr.Circle(gr.Point(coords[0], coords[1]), 25)
        cloud.setFill('white')
        cloud.draw(window)
        clouds.append(cloud)
    return cloud


def draw_house():
    house = gr.Rectangle(gr.Point(250, 150), gr.Point(450, 350))
    house.draw(window)
    house.setWidth(5)
    house.setFill('grey')

    glass_coords = [
                        [(300, 190), (350, 240)],
                        [(350, 190), (400, 240)],
                        [(300, 240), (350, 290)],
                        [(350, 240), (400, 290)]
                    ]

    for coords in glass_coords:
        glass = gr.Rectangle(gr.Point(coords[0][0], coords[0][1]),
                             gr.Point(coords[1][0], coords[1][1]))
        glass.setFill('yellow')
        glass.setWidth(5)
        glass.draw(window)

    roof = gr.Polygon(gr.Point(250, 150), gr.Point(450, 150), gr.Point(350, 80))
    roof.setFill('brown')
    roof.setWidth(5)
    roof.draw(window)


def draw_trunk(x, y):
    trunk = gr.Rectangle(gr.Point(x, y), gr.Point(x + 10, y + 100))
    trunk.setWidth(5)
    trunk.setFill('brown')
    trunk.draw(window)


def draw_needles(x, y):
    needles = gr.Polygon(gr.Point(x,       y + 80),
                         gr.Point(x + 85,  y),
                         gr.Point(x + 170, y + 80))
    needles.setFill('green')
    needles.setWidth(5)
    needles.draw(window)


window = gr.GraphWin("Landscape", 1000, 500)

# Рисуем небо
draw_sky()

# Рисуем землю
draw_ground()

# Рисуем солнце
sun = draw_sun(750, 100)

# Рисуем облака
clouds = list()

draw_clouds()

# Рисуем дом
# Стены, окна, крыши
draw_house()

# Рисуем дерево
draw_tree()

##############################################

window.getMouse()
window.close()
