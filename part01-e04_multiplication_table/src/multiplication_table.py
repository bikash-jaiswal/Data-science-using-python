#!/usr/bin/env python3


def main():
    for i in range(10):
        for j in range(10):
            print(f"{(i+1)*(j+1):3d} ", end="")
        print("")    
    pass

if __name__ == "__main__":
    main()
