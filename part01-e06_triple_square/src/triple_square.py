#!/usr/bin/env python3
def triple(value):
    """multiplies its parameter by three"""
    return value*3

def square(value):
    """raises its parameter to the power of two"""
    return value**2
def main():
    for i in range(1,11):
        x = square(i)
        y = triple(i)
        if(x>y):
            break
        else:
            print(f"triple({i})=={y} square({i})=={x}")

if __name__ == "__main__":
    main()
