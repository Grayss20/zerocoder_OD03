mas = [5, 7, 4, 3, 8, 2, 5]


# O(n^2) так как 2 вложенных цикла, дающих ~ n*n/2 = O(n^2)
def buble_sort(mas):
    for i in range(len(mas) - 1):
        for j in range(len(mas) - i - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return mas


# O(n * log(n)) так как в сортировке перемещается каждый элемент, и происходит дробление на 2 (3) части
def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    pivot = mas[0]
    left = [x for x in mas if x < pivot]
    middle = [x for x in mas if x == pivot]
    right = [x for x in mas if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# O(n^2) так как 2 вложенных цикла, дающих ~ n*n/2 = O(n^2)
def selection_sort(mas):
    for i in range(len(mas) - 1):
        min_index = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[min_index]:
                min_index = j
        mas[i], mas[min_index] = mas[min_index], mas[i]
    return mas


# O(n^2) так как 2 вложенных цикла, дающих ~ n*n/2 = O(n^2)
def insert_sort(mas):
    for i in range(1, len(mas)):
        key = mas[i]
        j = i - 1
        while j >= 0 and mas[j] > key:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key
    return mas


print(buble_sort(mas))
print(quick_sort(mas))
print(selection_sort(mas))
print(insert_sort(mas))
