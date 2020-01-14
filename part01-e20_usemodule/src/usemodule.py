#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    triangle.area(2, 5)
    triangle.hypothenuse(1, 1)
    print(triangle.__version__)
    print(triangle.__doc__)
    print(triangle.__author__)
    # Call the functions from here


if __name__ == "__main__":
    main()
