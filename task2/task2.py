import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline().strip())
    return (x, y), radius

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            points.append(tuple(map(float, line.split())))
    return points

def point_position(circle_center, radius, point):
    x_center, y_center = circle_center
    x, y = point
    
    # Корректное вычисление расстояния
    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
    
    if math.isclose(distance, radius):
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

def main():

    circle_file = r'C:\Users\Bartin\Desktop\Proba\test_rabota\task2\circle.txt'
    points_file = r'C:\Users\Bartin\Desktop\Proba\test_rabota\task2\points.txt'
    

    circle_center, radius = read_circle_data(circle_file)
    points = read_points(points_file)
    

    for point in points:
        position = point_position(circle_center, radius, point)
        print(position)

if __name__ == "__main__":
    main()