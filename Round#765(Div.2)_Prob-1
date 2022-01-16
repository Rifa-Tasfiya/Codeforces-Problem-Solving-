"""Code Forces Round #765 (Div.2)"""
"""Problem-A: Ancient Civilization"""
"""
Step-1: Convert all the decimal values into binary
Step-2: Count ones and zeros at each index of the binary value and store them in an array
Step-3: if count of ones at each index > count of zeros; add '1'. Otherwise, add '0'. This will be minimal nearness.
Step-4: Convert the minimal nearness into decimal
"""


def returnMinimalNearness(arr):
    binary_arr = []  # Storing all the decimal values in binary form
    for elem in arr:
        binary_val = decimalToBinary(int(elem))  # Convert decimal to binary
        binary_arr.append(binary_val)
    return minimalNearness(binary_arr)  # Return the minimal nearness


def decimalToBinary(num):
    temp_bnr = ""
    temp_num = num
    while temp_num != 0:
        temp_bnr += str(temp_num % 2)
        temp_num = temp_num // 2
    bnr_size = len(temp_bnr)
    for i in range(size - bnr_size):
        temp_bnr += "0"
    return temp_bnr[::-1]


def binaryToDecimal(num):
    decimal_val = 0
    for i in range(len(num)):
        if num[i] == "0":
            decimal_val = decimal_val * 2
        else:
            decimal_val = decimal_val * 2 + 1
    return decimal_val


def minimalNearness(arr):
    count_zero_lst = []
    count_one_lst = []
    for i in range(size):
        arr_idx = 0
        count_zero = 0
        count_one = 0
        while arr_idx != num:
            if arr[arr_idx][i] == "0":
                count_zero += 1
            else:
                count_one += 1
            arr_idx += 1
        count_one_lst.append(count_one)
        count_zero_lst.append(count_zero)
    minimal_nearness_bnr = ""
    for i in range(size):
        if count_one_lst[i] > count_zero_lst[i]:
            minimal_nearness_bnr += "1"
        else:
            minimal_nearness_bnr += "0"
    nearness = binaryToDecimal(minimal_nearness_bnr)
    return nearness


# ========================================For user input================================================================
t = int(input())  # Number of test cases
for i in range(t):
    num_size = input().split()  # Number of decimal values, Binary bit
    num, size = int(num_size[0]), int(num_size[1])
    arr = input().split()  # Storing decimal numbers in the array
    print(returnMinimalNearness(arr))
