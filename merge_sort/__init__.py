import math


def start_sort():
    with open('merge_sort/numbers.txt') as f1:
        numbers = [num for line in f1 for num in line.split()]

    sorted_numbers = merge_sort(numbers)
    print(sorted_numbers)


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers[0]

    half = math.ceil(len(numbers) / 2)

    left_half = numbers[:half]
    right_half = numbers[half:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge_numbers(sorted_left, sorted_right)


def merge_numbers(lef, rig):
    c = []
    i = 0
    j = 0

    while i != len(lef) and j != len(rig):
        if lef[i] < rig[j]:
            c.append(lef[i])
            i += 1
        else:
            c.append(rig[j])
            j += 1

    if len(rig) == j:
        c += lef[i:]
    else:
        c += rig[j:]

    return c
