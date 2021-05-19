#!/usr/bin/env python3
#coding: utf-8

from zencad import *

D = 18
ELEM_SIZE = 19
HEIGHT = 4
SPACING_R = 2
#10s6p
S = 10
P = 6


m = (
    box(ELEM_SIZE, ELEM_SIZE, HEIGHT, center=True).translate(z=HEIGHT/2) -
    cylinder(SPACING_R, HEIGHT).translate(-ELEM_SIZE/2, -ELEM_SIZE/2) -
    cylinder(SPACING_R, HEIGHT).translate(-ELEM_SIZE/2, ELEM_SIZE/2) -
    cylinder(SPACING_R, HEIGHT).translate(ELEM_SIZE/2, -ELEM_SIZE/2) -
    cylinder(SPACING_R, HEIGHT).translate(ELEM_SIZE/2, ELEM_SIZE/2)
)
c = cylinder((D+0.5)/2, HEIGHT)
h = cylinder((D+0.5)/2, 1) - cylinder((D-2)/2, HEIGHT)
elem = m - c +h
a = []
for i in range(0, S):
    for j in range(0, P):
        a.append(elem.translate(i*ELEM_SIZE, j*ELEM_SIZE))

res = union(a)
print(f'X size: {res.bbox().xmax-res.bbox().xmin}, Y size: {res.bbox().ymax-res.bbox().ymin}')
to_stl(res, './18650.stl', 0.55)
disp(res)

show()
