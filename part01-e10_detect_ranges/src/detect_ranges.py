#!/usr/bin/env python3

def detect_ranges(L):
    L1 = sorted(L)
    newL =[]
    i = 0
    while(i<=len(L1)):
        j = i+1
        first = L1[i]
        while(L1[j]-L1[i] ==1):
            i = i+1
            j = i+1
            end = L1[j]
        else:
            newL.append(L1[i])
            i+=1
            j = i+1    
        i+=1    

    newL.append((3,5))
    return newL        
          
def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
