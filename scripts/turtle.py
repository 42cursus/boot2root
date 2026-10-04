#!/usr/bin/env python

import os
import re
import sys

# This file is also named turtle.py. Remove its directory from the import
# path so the next import finds Python's standard-library turtle module.
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [p for p in sys.path if os.path.abspath(p or os.getcwd()) != script_dir]
import turtle as t

if len(sys.argv) != 2:
    raise SystemExit("usage: python scripts/turtle.py <downloaded-turtle-file>")

def parse(linha):
    num = re.search(r'(\d+)', linha)
    n = int(num.group(1)) if num else 0

    if "Avance" in linha:
        return ("forward", n)
    elif "gauche" in linha:
        return ("left", n)
    elif "droite" in linha:
        return ("right", n)
    elif "Recule" in linha:
        return ("backward", n)
    return None

screen = t.Screen()
screen.tracer(0)

t.penup()
t.goto(-300, 0)
t.pendown()

with open(sys.argv[1]) as file:
    for line in file:
        if line.strip() == "":
            heading = t.heading()   # stores the current heading
            t.penup()
            t.setheading(0)         # points to the right
            t.forward(250)          # spacing between letters (adjust if needed)
            t.setheading(heading)   # restores the heading
            t.pendown()
            continue

        # print(line.rstrip())
        parsed_line = parse(line)
        if parsed_line:
            action, value = parsed_line
            getattr(t, action)(value)

screen.update()
t.done()
