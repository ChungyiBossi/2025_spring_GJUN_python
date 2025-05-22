def binary_search(sorted_numbers, target):
    start_index = 0
    end_index = len(sorted_numbers)-1
    target_index = -1  # 假設在序列之外
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2
        if sorted_numbers[mid_index] == target:
            target_index = mid_index  # 找到目標
            break  # 離開迴圈
        elif sorted_numbers[mid_index] < target:
            # 找右半邊
            start_index = mid_index + 1
        else:
            # 找左半邊
            end_index = mid_index - 1

    return target_index


if __name__ == '__main__':
    result = binary_search([10, 15, 20, 40, 55, 80], 55)
    print('Find 55 at ', result)

    result = binary_search([10, 15, 20, 40, 55, 80], 20)
    print('Find 20 at ', result)

    result = binary_search([10, 15, 20, 40, 55, 80], 99)
    print('Find 99 at ', result)
