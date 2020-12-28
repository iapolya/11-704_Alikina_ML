import pygame as pg
from sklearn import svm

WHITE = (255, 255, 255)
PINK = (255, 192, 203)
YELLOW = (225, 225, 0)
GREEN = (0, 225, 0)

sc = pg.display.set_mode((400, 400))
sc.fill(WHITE)
pg.display.update()

dots = {}
colors = []

exit_flag = True


def new_point(colors, button):
    colors.append(button)
    pg.display.update()


while exit_flag:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit_flag = False
        elif i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                # ЛЕВАЯ = РОЗОВАЯ
                pg.draw.circle(sc, PINK, i.pos, 5)
                dots[i.pos] = PINK
                new_point(colors, i.button)
            elif i.button == 3:
                # ПРАВАЯ = ЖЕЛТАЯ
                pg.draw.circle(sc, YELLOW, i.pos, 5)
                dots[i.pos] = YELLOW
                new_point(colors, i.button)

        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_RETURN:
                sc.fill(WHITE)
                for dot, dot_color in dots.items():
                    pg.draw.circle(sc, dot_color, dot, 5)
                clf = svm.SVC(kernel='linear', C=1.0)
                clf.fit(tuple(dots.keys()), colors)
                w = clf.coef_[0]
                i = clf.intercept_
                n = -w[0] / w[1]
                m = i[0] / w[1]
                y1 = -m
                x1 = m / n
                reversed_coef = tuple(map(lambda x: 1 / x, w))
                y2, x2 = (reversed_coef[1] + y1,
                          reversed_coef[0] + x1)
                y3, x3 = (-reversed_coef[1] + y1,
                          -reversed_coef[0] + x1)
                k = - y1 / x1
                end = 0 if k < 0 else 400

                pg.draw.line(sc, GREEN, [0, y1], [(end - y1) / k, end], 1)
                pg.draw.aaline(sc, GREEN, [0, y2], [(end - y2) / k, end])
                pg.draw.aaline(sc, GREEN, [0, y3], [(end - y3) / k, end])
                pg.display.update()


            elif i.key == pg.K_SPACE:
                sc.fill(WHITE)
                dots = {}
                colors = []
                pg.display.update()

    pg.time.delay(30)
