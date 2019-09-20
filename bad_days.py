#!/usr/bin/python

# https://codeforces.com/problemset/problem/1203/B

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

        area = -1
        n = 0
        valid = True
        for i in range(len(seq)/2):
            a = seq[n] * seq[len(seq) - n - 1]
            #print(a)
            if i == 0:
                area = a

            if a != area:
                valid = False
                break

            area = a
            n += 2

        if valid == False:
            print "NO"
        else:
            print "YES"
