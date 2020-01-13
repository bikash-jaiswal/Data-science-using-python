#!/usr/bin/env python3


def main():
    two_dice = [(i, j) for i in range(1, 7)
                for j in range(1, 7)
                if i + j == 5]
    for x in two_dice:
        print(x)
    pass


if __name__ == "__main__":
    main()
