#!/usr/bin/env python3

import math

def positive_root(a,b,c):
    return (-b + math.sqrt(b**2 - 4*a*c))/(2*a)

def negative_root(a,b,c):
    return (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

def solve_quadratic(a, b, c):
    positive = positive_root(a,b,c)
    negative = negative_root(a,b,c)
    return (positive,negative)


def main():
    print(solve_quadratic(1,-3,2))

if __name__ == "__main__":
    main()
