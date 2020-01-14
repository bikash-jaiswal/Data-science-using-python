#!/usr/bin/env python3


def sum_equation(L):
    string = ""
    if len(L) == 0:
        return "0 = 0"
    else:
        string = " + ".join([str(x) for x in L])
    return " = ".join([string, str(sum(L))])


def main():
    print(sum_equation([1, 5, 7]))
    pass


if __name__ == "__main__":
    main()
