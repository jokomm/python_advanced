import importlib

calculate_circle = importlib.import_module("circle_pkg.circle")


def main():
    R = float(input("Enter the radius of the circle : "))
    while R < 0:
        R = float(input("Error: Enter a positive radius of the circle : "))

    solution = calculate_circle.calculate_circle(R)

    print(solution)


if __name__ == '__main__':
    main()