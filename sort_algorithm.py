def bubble_sort(numbers):
    for r in range(len(numbers)-1):
        for i in range(len(numbers)-1-r):  # 多扣r
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        print("Round ", r, numbers)
    return numbers


def selection_sort(numbers):
    for r in range(len(numbers)):
        min_idx = r
        for i in range(r, len(numbers)):
            if numbers[i] < numbers[min_idx]:
                min_idx = i
        if min_idx != r:
            numbers[r], numbers[min_idx] = numbers[min_idx], numbers[r]
        print("Round ", r, numbers)
    return numbers


def merge(sorted_left, sorted_right):
    sorted_numbers = list()
    print('Start: ', sorted_left, sorted_right, sorted_numbers)
    while len(sorted_left) > 0 and len(sorted_right) > 0:
        if sorted_left[0] < sorted_right[0]:  # 左頭 < 右頭
            # list.pop(index) 表示移除並回傳移除值
            sorted_numbers.append(sorted_left.pop(0))
        else:
            sorted_numbers.append(sorted_right.pop(0))

        print(sorted_left, sorted_right, sorted_numbers)

    if len(sorted_left) > 0:
        sorted_numbers = sorted_numbers + sorted_left
    else:  # len(sorted_right) > 0
        sorted_numbers = sorted_numbers + sorted_right

    return sorted_numbers


def merge_sort(numbers):

    if len(numbers) < 2:  # length == 0 or 1
        return numbers

    # Divide
    mid_index = len(numbers)//2  # 整除
    left_part = numbers[0:mid_index]  # 0 ~ (mid_index - 1)
    right_part = numbers[mid_index:]  # mid_index ~ 最後

    # Conquer (merge)
    # sorted_left = sorted(left_part)
    # sorted_right = sorted(right_part)
    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)
    sorted_numbers = merge(sorted_left, sorted_right)
    return sorted_numbers


def insertion_sort(numbers):
    for round in range(len(numbers)-1):
        new = numbers[round+1]
        old_idx = round

        # 在尚未比到頭(old_idx >= 0) 且 new 還小於時 繼續
        while old_idx >= 0 and new <= numbers[old_idx]:
            numbers[old_idx + 1] = numbers[old_idx]  # 不是交換
            old_idx -= 1
        numbers[old_idx+1] = new

    sorted_numbers = numbers
    return sorted_numbers


if __name__ == '__main__':

    result = insertion_sort([40, 30, 60, 50, 20])
    print(result)
