#!/usr/bin/env python3


def reverse_dictionary(d):
    new_d = {}
    for key in d.keys():
        for values in d[key]:
            if values in new_d.keys():
                #print("I already exist")
                new_d[values].append(key)
            else:
                new_d[values] = [key]
    return new_d


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa',
                                         'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    pass


if __name__ == "__main__":
    main()
