class Bullet:
    def __init__(self, name, mass, bc, speed):
        self.name = name
        self.mass = mass
        self.bc = bc
        self.speed = speed

    def __str__(self):
        return f"{self.name}: mass={self.mass} kg, BC={self.bc}, speed={self.speed} m/s"
BULLETS = [
    Bullet("9mm", 0.008, 0.15, 380),
    Bullet("308_win", 0.00945, 0.45, 820),
    Bullet("556_nato", 0.004, 0.3, 950),
    Bullet("762x39", 0.008, 0.275, 715)
]