import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600

# цвета выбраны с сайта: https://htmlcolorcodes.com/
BLUE = (30, 51, 109)
PURPLE = (121, 59, 135)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 168, 0)
FIRE = (222, 24, 18)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(PURPLE)  # заливка фона
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.polygon(screen, BLUE, [[WIDTH - 990, 500], [WIDTH - 990, 100], [WIDTH - 10, 500], [WIDTH - 10, 100]])
pg.draw.rect(screen, ORANGE, [WIDTH / 4, HEIGHT / 4, WIDTH / 2, HEIGHT / 2])
pg.draw.circle(screen, FIRE, (WIDTH / 2, HEIGHT / 2), 50)
pg.draw.line(screen, FIRE, [WIDTH / 2, HEIGHT / 2], [WIDTH / 4 + WIDTH / 2, HEIGHT / 4 + HEIGHT / 2], 10)
pg.draw.line(screen, FIRE, [WIDTH / 2, HEIGHT / 2], [WIDTH / 4, HEIGHT / 4], 10)
pg.draw.line(screen, FIRE, [WIDTH / 2, HEIGHT / 2], [WIDTH / 4, HEIGHT / 4 + HEIGHT / 2], 10)
pg.draw.line(screen, FIRE, [WIDTH / 2, HEIGHT / 2], [WIDTH / 4 + WIDTH / 2, HEIGHT / 4], 10)
pg.draw.lines(screen, BLACK, True,[[WIDTH / 3, HEIGHT / 3], [WIDTH / 1.5, HEIGHT / 3], [WIDTH / 1.5, HEIGHT / 1.5], [WIDTH / 3, HEIGHT / 1.5]], 2)




# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
