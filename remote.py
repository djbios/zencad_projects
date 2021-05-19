#!/usr/bin/env python3
# coding: utf-8

from zencad import *

REMOTE_THICK = 27
REMOTE_WIDTH = 55
HEIGHT = 80
WALL = 2
BOLT_D = 2

m = box(REMOTE_WIDTH + 2 * WALL, REMOTE_THICK + 2 * WALL, HEIGHT + WALL)
r = box(REMOTE_WIDTH, REMOTE_THICK, HEIGHT).translate(WALL, WALL, WALL)
res = m - r
line = sew(
    [
        interpolate(
            [
                (REMOTE_WIDTH / 4, 0, HEIGHT + WALL),
                (2 * REMOTE_WIDTH / 4, 0, WALL*3),
                (3 * REMOTE_WIDTH / 4, 0, HEIGHT + WALL),
            ]
        ),
        segment(
            (3 * REMOTE_WIDTH / 4, 0, HEIGHT + WALL),
            (REMOTE_WIDTH / 4, 0, HEIGHT + WALL),
        ),
    ]
)
hole = extrude(fill(line), (0, WALL, 0)).translate(WALL, 0, 0)
res = res - hole
res = res.fillet(WALL/3)

s = (
    cone(BOLT_D/2, BOLT_D*1.5, WALL*1.1 , center=True)
    .rot(3.14 / 2, 0, 0)
    .translate(REMOTE_WIDTH / 2 + WALL, REMOTE_THICK + WALL + 1, 3 * HEIGHT / 4)
)
res = res - s

res = res - s.translate(0,0,-HEIGHT/3)
to_stl(res,'./remote.stl', 0.55)
disp(res)
show()

