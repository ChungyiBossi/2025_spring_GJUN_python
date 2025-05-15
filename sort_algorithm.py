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


if __name__ == '__main__':
    numbers = [40, 30, 60, 50, 20]
    selection_sort(numbers)
