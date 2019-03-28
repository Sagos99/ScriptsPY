# -*- coding: utf-8 -*-

num = 82

for x in range(7):
    print(num)
    for x in range(2):
        num += 28
        print(num)

        num -= 13
        print(num)

        num += 28
        num *= 2
        print(num)
        num -= 13