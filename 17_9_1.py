first_num = list(map(int, input('Введите числа через пробел ').split()))
second_num = int(input('Введите одно число '))
first_num.append(second_num)

def sorting(list):
    for i in range(len(first_num)):
        for j in range(len(first_num) - i - 1):
            if first_num[j] > first_num[j + 1]:
                first_num[j], first_num[j + 1] = first_num[j + 1], first_num[j]
    return list

print('Сортированный по возрастанию список:', sorting(first_num))
sort_first_num = sorting(first_num)

element = second_num
array = sort_first_num

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print('Индекс введенного числа ', binary_search(array, element, 0, len(array)-1))