#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2. Ввести список А из 10 элементов, найти произведение положительных элементов
# и вывести его на экран.


import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Найти искомое произведение.
    S = 1
    for item in A:
        if item > 0:
            S *= item

    print(S)