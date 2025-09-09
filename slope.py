def slope(point1:tuple[int], point2:tuple[int]):
    x1, y1 = point1
    x2, y2 = point2

    delta_y = y2 - y1
    delta_x = x2 - x1
    m = f"{delta_y} / {delta_x}"
    return m


if __name__ == "__main__":
    print(f"""
CALCULATE SLOPE:
Enter points as a tuple (e.g. (1,2) and (2,1))
""")
    point1 = input("Point 1: ")
    point2 = input("Point 2: ")

    point1 = tuple([int(p) for p in point1[1:-1].split(",")])
    point2 = tuple([int(p) for p in point2[1:-1].split(",")])

    m = slope(point1, point2)
    print(m)
