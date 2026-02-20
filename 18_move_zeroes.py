# Question 18: Move Zeroes to End
def move_zeroes(arr):
    non_zero = [x for x in arr if x != 0]
    return non_zero + [0] * (len(arr) - len(non_zero))

if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print(move_zeroes(arr))