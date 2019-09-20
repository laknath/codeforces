#!/usr/bin/python

# https://codeforces.com/problemset/problem/1203/B

def area(seq, n):
    """Generates the area of a rectangle.

    Given a sequence of ordered edges in seq, calculate the area
    of a rectangle using (n, len(seq) - i) edge pair.

    Args:
        seq: An ordered list of integers
        n: The edge index. 

    Returns:
        The area using (n, len(seq)-i) edge pairs.
    """
        
    return seq[n] * seq[len(seq) - n - 1]

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        sticks = {}

        nn = int(input())
        seq = map(int, raw_input().split())
        seq.sort()

        for x in seq:
            if x in sticks:
                sticks[x] += 1
            else:
                sticks[x] = 1

        valid = True 
        for k, v in sticks.items():
            if v % 2 != 0:
                valid = False
                break

        if valid == False:
            print "NO"
            continue

        a = area(seq, 0)
        n = 0
        valid = True
        for i in range(1, len(seq)/2):
            a_ = area(seq, i)
            #print(a)

            if a_ != a:
                valid = False
                break

            a = a_
            n += 2

        if valid == False:
            print "NO"
        else:
            print "YES"
