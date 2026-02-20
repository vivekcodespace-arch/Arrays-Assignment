def max_product_pair(arr):
    if len(arr) < 2:
        return None
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    return max(max1 * max2, min1 * min2)

if __name__ == "__main__":
    arr = [-10, -3, 5, 6, -2]
    print(max_product_pair(arr))