import sys; sys.path.insert(0,"/home/user/Claude/Projekty/Osobni/Outputs/tetovani-blizenci")
from generator import *
W,H=600,320
p=[f'<rect width="{W}" height="{H}" fill="#fff"/>']
p.append(glyph("K", 90, 70, 180, w=3.0))
p.append(glyph("O", 300, 70, 180, w=3.0))
p.append(f'<line x1="0" y1="70" x2="{W}" y2="70" stroke="#eee"/>')
p.append(f'<line x1="0" y1="250" x2="{W}" y2="250" stroke="#eee"/>')
open("/tmp/claude-0/-home-user-Claude/aac46e82-215b-57f5-89f5-bd00dc612075/scratchpad/g.svg","w").write(
 f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+"\n".join(p)+'</svg>')
