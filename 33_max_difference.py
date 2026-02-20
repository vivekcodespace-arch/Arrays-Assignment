# Question 33: Find Maximum Difference
def max_difference(arr):
    if len(arr) < 2:
        return 0
    min_val = arr[0]
    max_diff = float('-inf')
    for num in arr[1:]:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)
    return max_diff

if __name__ == "__main__":
    arr = [2, 3, 10, 6, 4, 8, 1]
    print(max_difference(arr))