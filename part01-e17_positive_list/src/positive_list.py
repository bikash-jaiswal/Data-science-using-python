#!/usr/bin/env python3


def is_positive(x):
    """ return true if x is positive"""
    return x > 0


def positive_list(L):
    """return list of positive number"""
    return list(filter(is_positive, L))


def main():
    print(positive_list([2, -2, 0, 1, -7]))
    pass


if __name__ == "__main__":
    main()
