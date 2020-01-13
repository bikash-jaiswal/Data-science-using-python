#!/usr/bin/env python3

def transform(s1, s2):
    L1 = s1.split()
    L2 = s2.split()

    return [i*j for i,j in zip(map(int,L1),map(int,L2))]

def main():
    print(transform("1 2 30", "2 4 1"))
    pass

if __name__ == "__main__":
    main()
