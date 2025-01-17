import math
import matplotlib.pyplot as plt
from main_direct.balistik import *
from bullet.types_bull import BULLETS
from balistik_helper.drag import drag_coefficient

def ballistic_calculator_bullet(initial_speed, angle_deg, BC, bullet_mass, gravity=9.81, air_density=1.225, wind_speed=0, temp=15, distance_limit=1000):
    angle_rad = math.radians(angle_deg)
    speed_x = initial_speed * math.cos(angle_rad)
    speed_y = initial_speed * math.sin(angle_rad)
    time_step = 0.001
    x, y = 0, 0
    trajectory_x = [x]
    trajectory_y = [y]

    # Коррекция плотности воздуха по температуре
    air_density *= 273.15 / (273.15 + temp)

    while y >= 0 and x <= distance_limit:
        speed = math.sqrt(speed_x ** 2 + speed_y ** 2)
        mach_speed = speed / 343  # Скорость в числах Маха (343 м/с - скорость звука)
        Cd = drag_coefficient(mach_speed)
        drag_force = 0.5 * air_density * Cd * (speed ** 2) / BC

        acc_x = -(drag_force / bullet_mass) * (speed_x / speed) + wind_speed / bullet_mass
        acc_y = -gravity - (drag_force / bullet_mass) * (speed_y / speed)

        speed_x += acc_x * time_step
        speed_y += acc_y * time_step

        x += speed_x * time_step
        y += speed_y * time_step

        trajectory_x.append(x)
        trajectory_y.append(y)

    plt.figure(figsize=(10, 5))
    plt.plot(trajectory_x, trajectory_y)
    plt.title("Ballistic Trajectory for Bullet (with Air Drag)")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True)
    plt.show()

# Функция для выбора пули и запуска расчетов
def main():
    print("Выберите тип пули:")
    for i, bullet in enumerate(BULLETS):
        print(f"{i + 1}. {bullet}")

    bullet_choice = int(input("Введите номер пули: ")) - 1
    if bullet_choice < 0 or bullet_choice >= len(BULLETS):
        print("Неправильный выбор пули!")
        return

    bullet = BULLETS[bullet_choice]
    angle_deg = float(input("Введите угол выстрела (в градусах): "))
    wind_speed = float(input("Введите скорость ветра (м/с): "))
    temp = float(input("Введите температуру воздуха (°C): "))
    distance_limit = float(input("Введите максимальную дальность полета (м): "))

    ballistic_calculator_bullet(bullet.speed, angle_deg, bullet.bc, bullet.mass, wind_speed=wind_speed, temp=temp, distance_limit=distance_limit)

if __name__ == "__main__":
    main()

# Функция для выбора пули и запуска расчетов
def main():
    print("Выберите тип пули:")
    for i, bullet in enumerate(BULLETS):
        print(f"{i + 1}. {bullet}")

    bullet_choice = int(input("Введите номер пули: ")) - 1
    if bullet_choice < 0 or bullet_choice >= len(BULLETS):
        print("Неправильный выбор пули!")
        return

    bullet = BULLETS[bullet_choice]
    angle_deg = float(input("Введите угол выстрела (в градусах): "))

    ballistic_calculator_bullet(bullet.speed, angle_deg, bullet.bc, bullet.mass)

main()