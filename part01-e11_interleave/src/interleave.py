#!/usr/bin/env python3

def interleave(*lists):
    output = list(zip(*lists))
    return [item for listt in output for item in listt]
    

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
