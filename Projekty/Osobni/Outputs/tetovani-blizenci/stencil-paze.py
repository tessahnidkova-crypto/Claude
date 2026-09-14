#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ciste podklady na PAZI pro tatera: cerna na bile, bez popisku, vektor."""
import sys
sys.path.insert(0, "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *
from paze import v1, v2, v3

W = 520
base = "/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci/"

def wrap(body, H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#fff"/>'
            + body.replace('#111', '#000') + '</svg>')

open(base + "paze-stencil-1.svg", "w").write(wrap(v1(W/2, 50, 400), 940))
open(base + "paze-stencil-2.svg", "w").write(wrap(v2(W/2, 50, 400), 960))
open(base + "paze-stencil-3.svg", "w").write(wrap(v3(W/2, 50, 320), 830))
print("paze-stencil-1/2/3.svg")
