from math import atan2, pi


xa, ya, xb, yb = map(int, input().split())
ra = (xb ** 2 + yb ** 2) ** 0.5
rb = (xa ** 2 + ya ** 2) ** 0.5

if ra == 0 or rb == 0:
    print("{:.6f}".format(ra + rb))
else:
    alpha = atan2(ya, xa)
    beta = atan2(yb, xb)
    if alpha < 0:
        alpha += 2 * pi
    if beta < 0:
        beta += 2 * pi
    print("{:.6f}".format(min(min(ra, rb) * abs(alpha - beta) + abs(ra - rb), ra + rb)))
