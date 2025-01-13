import math
G1_TABLE = [
    (0, 1.0000), (0.5, 0.9800), (1.0, 0.8800), (1.5, 0.7800),
    (2.0, 0.7000), (2.5, 0.6300), (3.0, 0.5700), (3.5, 0.5200),
    (4.0, 0.4800), (4.5, 0.4500), (5.0, 0.4300)
]

def drag_coefficient(speed_mach):
    for i in range(len(G1_TABLE) - 1):
        if G1_TABLE[i][0] <= speed_mach < G1_TABLE[i + 1][0]:
            x1, y1 = G1_TABLE[i]
            x2, y2 = G1_TABLE[i + 1]
            return y1 + (y2 - y1) * (speed_mach - x1) / (x2 - x1)
    return G1_TABLE[-1][1]